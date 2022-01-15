# from django.views import View
from itertools import product
from django import views
from product.models.product import Product

from django.shortcuts import render

class Product_by_category(views.View):
    def get(self,request,cat):

        productByCategory=Product.objects.filter(category=cat)
        products=Product.objects.all()

        categories=set()

        for p in products:
            categories.add(p.category)

        return render(request,'jberry/trending.html' ,{'products':productByCategory,'category':categories})
