from __future__ import unicode_literals

from django.db import models
COLOR_CHOICES = (
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('W', 'White'),
)
class Customer(models.Model):
	firstname=models.CharField( max_length=10 )
	lastname=models.CharField( max_length=10 )
	tel=models.CharField( max_length=10 )

class Car(models.Model):
	model=models.CharField( max_length=10 )
	color=models.CharField( max_length=1, choices=COLOR_CHOICES)

class Rent(models.Model):
	car=models.ForeignKey( 'Car' , on_delete=models.CASCADE)
	custom=models.ForeignKey( 'Customer' , on_delete=models.CASCADE)