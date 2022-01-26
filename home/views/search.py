import re
from django import views

from django.shortcuts import render

from product.models import Product
from django.http import HttpResponse

class Search(views.View):
    def get(self,request):

        all_product=Product.objects.all().order_by('-id')

        return render(request,'Jberry/index.html',{"product":all_product})

    def post(self,request):
        queary=request.POST.get('search').split(' ')
        print("QUEARYYYYYYYYYYYYYYYYYYY", queary)
        result=Product.objects.filter(title__icontains=queary[0])
        result=result.union(Product.objects.filter(description__icontains=queary[0]))

        for q in queary:
            result=result.union(Product.objects.filter(title__icontains=q))
            result=result.union(Product.objects.filter(description__icontains=q))

        if not queary:
            all_product=Product.objects.all().order_by('-id')
        else:
          all_product=result
        return render(request,'Jberry/index.html',{"product":all_product})