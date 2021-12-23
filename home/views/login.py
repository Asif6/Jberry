from django import views
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View


class Login(views.View):
    def get(self, request):
        return render(request, 'Jberry/login.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        valid_user = authenticate(username=username, password=password)

        if valid_user:
            login(request, valid_user)
            return redirect("index")
        else:
            messages.error(request,  "No Account found ")
            return render(request, 'Jberry/login.html')


class Logout(views.View):
    def get(self, request):
        logout(request)
        return redirect('index')
