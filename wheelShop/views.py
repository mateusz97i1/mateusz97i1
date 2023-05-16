from django.shortcuts import render, redirect 
from django.views.generic import TemplateView,ListView,View
import datetime
from django import template
from .models import WheelsModel
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from authlib.integrations.django_client import OAuth

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
import json
from django.conf import settings
import stripe
from django.urls import reverse, reverse_lazy
import os
from decouple import config
register = template.Library()




# Create your views here.
#Main site page, additionally show clock at the right top corner
class MainView(TemplateView):
    template_name='mainHero.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = self.clock()
        return context
    
    @staticmethod
    def clock():
            
        return datetime.datetime.now()
    
def searched(request):

    if request.method == 'GET' and 'searchMain' in request.GET and request.GET['searchMain']:
        parts = request.GET['searchMain']
        wheelSearch = WheelsModel.objects.filter(name__icontains=parts)
        return render(request, "searched.html", {'parts': wheelSearch})
    else:
       
        return render(request, "searched.html")

    
   
#Displays all wheels from database
def parts(request):


    wheels = WheelsModel.objects.all()
    context = {'wheels': wheels}
    return render(request, 'parts.html', context)


class AboutView(TemplateView):
    template_name='about.html'

#logout
# https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}

#Logging Out function from Auth0
def logout(request):
    django_logout(request)

    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='https://mateusz97i1wheelsshop.vercel.app/'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")
    

#user profile Auth0
def profile(request):
    user=request.user

    auth0_user=user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name': auth0_user.extra_data.get(''),
    }

    context={
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }

    return render(request,'profile.html',context)

#basket, What we already have bought
def shoppingBasket(request):


    cart = request.session.get('cart', {})
    wheel_items = []
    total = 0
    # Adds a clear button, if is clicked then the session request, cart/basket will be cleared
    if request.POST:
        request.session['cart'] = {}
        return redirect('wheelShop:shoppingBasket')

    #Adding info to the request session liblary
    for wheel_id, quantity in cart.items():
        wheel = WheelsModel.objects.get(id=wheel_id)
        wheel_items.append({
            'id': wheel_id,
            'name': wheel.name,
            'image': wheel.image,
            'price': wheel.price,
            'quantity': quantity
        })
        #Counting total cost of the cart
        total += wheel.price * quantity

    context = {
        'wheel_items': wheel_items,
        'total': total
    }

    return render(request, 'shoppigBasket.html', context)
    
#add to cart function, saves in our sesion informations
#about bought items
def add_to_cart(request, wheel_id):

    wheel = WheelsModel.objects.get(id=wheel_id) #Takes id of the wheel from WHeelsSHop database

    amount=int(request.POST.get('amount',1)) # Read selected amount or take 1 as the default value

    cart = request.session.get('cart', {})
    cart[wheel_id] = cart.get(wheel_id, 0) + amount
    request.session['cart'] = cart

    return redirect('wheelShop:shoppingBasket')


def remove_from_cart(request,wheel_id):

    if request.method == 'POST':
        wheel_id = request.POST.get('wheel_id')
        cart = request.session.get('cart', {})
        
        if wheel_id in cart:
            del cart[wheel_id]
            request.session['cart'] = cart

    return redirect('wheelShop:shoppingBasket')


def payment_successful(request):
    return render(request,'success.html')


def payment_cancelled(request):
    return render(request,'cancel.html')


#Takes stripe secret key from setting.py
stripe.api_key=config('STRIPE_SECRET_KEY')

# @login_required
def checkout(request):

    #Gets The total price of the order
    cart = request.session.get('cart', {})
    total = 0

    #loop that counts items and returns total price of our basket/cart
    for wheel_id, quantity in cart.items():
        wheel = WheelsModel.objects.get(id=wheel_id)
        # New function removes bought items(reduces quantity) from the db
        wheel.leftOnStock-=quantity
        wheel.save() 
        total += wheel.price * quantity
        


    #Creating checkout session
    checkout_session = stripe.checkout.Session.create(

        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price_data':{
                    'unit_amount':total*100, # Multiplayed 100times because the price is in cents
                    'currency':'pln',
                    'product_data': {
                                    'name': 'Wheels',
                                    },
                }, 
                'quantity': 1,
            },
        ],
        
        mode='payment', #sub mode also u can change it to payment if u already have set it up for that purpose
        success_url=request.build_absolute_uri(reverse('wheelShop:payment_successful')),
        cancel_url=request.build_absolute_uri(reverse('wheelShop:payment_cancelled')),
    )
    #redirects to the stripe payment site
    return redirect(checkout_session.url, code=303)
