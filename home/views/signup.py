from django import views
from django.views import View

from django.shortcuts import render


class Signup(views.View):
    def get(self, request):
        return render(request, 'Jberry/signup.html')
