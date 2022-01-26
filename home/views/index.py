from django import views
from django.shortcuts import render
from django.views import View
from product.models import Product


class Index(views.View):

    def get(self, request):
        all_product=Product.objects.all().order_by('-id')

        data={}
        data['product']=all_product
        return render(request, 'Jberry/index.html',data)
