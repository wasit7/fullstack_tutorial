from django.contrib import admin
from models import Car,Customer,Rent
# Register your models here.

class CarAdmin(admin.ModelAdmin):
	list_display = ('model','color')

admin.site.register(Car, CarAdmin)
