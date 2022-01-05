from django import views
from django.shortcuts import render, redirect

from django.views import View


class Productindex(views.View):
    def get(self, request):
        return render(request, 'Jberry/trending.html')
