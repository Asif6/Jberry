from django import views

from django.shortcuts import render

from product.models.product import Product

class Product_details(views.View):
    def get(self,request,id):

        product=Product.objects.filter(id=id)
        

        return render(request,'jberry/product-details.html',{'product':product})