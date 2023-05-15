from django.urls import path,include
from . import views

app_name='wheelShop'

urlpatterns=[

    path('',views.MainView.as_view(),name='main'),
#     path('parts/',views.parts,name='partsy'),
#     path('about/',views.AboutView.as_view(),name='abouty'),
#     path('', include('social_django.urls', namespace='social')),
#     path('logout/',views.LogoutView.as_view(),name='logout'),
#     path('profile/',views.profile,name='profile'),
#     path('shopping-basket/',views.shoppingBasket,name='shoppingBasket'),
#     path('add-to-cart/<int:wheel_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove_from_cart/<int:wheel_id>/',views.remove_from_cart,name='remove_from_cart'),
#     path('payment_successful/',views.payment_successful,name='payment_successful'),
#     path('payment_cancelled/',views.payment_cancelled,name='payment_cancelled'),
#     path('checkout/',views.checkout,name='checkout'),
#     path('searched/',views.searched,name='searched'),

    
]

