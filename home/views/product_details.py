from django import views
from django.shortcuts import render
from product.models.product import Product

class Product_details_view(views.View):
    def get(self,request,id):

        product=Product.objects.filter(id=id)


        return render(request,'jbery/product-details.html',{'product',product})
