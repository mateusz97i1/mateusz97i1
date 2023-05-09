from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class WheelsModel(models.Model):
    name=models.CharField(max_length=50)
    size=models.IntegerField(validators=[MaxValueValidator(22)])
    price=models.IntegerField()
    leftOnStock=models.IntegerField()
    image=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
