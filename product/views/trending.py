from django.views import View
from django import views
from django.shortcuts import render

from product.models.product import Product

class Trending(views.View):
    def get(self,request):
        all_product=Product.objects.all().order_by('-id')

        category= set()
        for p in all_product:
            category.add(p.category)
        print(category)
        return render(request,'jberry/trending.html', {'products': all_product,'category':category})
