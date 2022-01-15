from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models.product import Product


# class AdminProduct(admin.ModelAdmin):
    # list_diplay=['id','title','description','price']

admin.site.register(Product)
