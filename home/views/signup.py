from django import views
from django.views import View

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class Signup(views.View):
    def get(self, request):
        return render(request, 'Jberry/signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        errormassage = None
        valid_user = User.objects.filter(username=user_name).exists()
        valid_email = User.objects.filter(email=email).exists()

        if valid_user or valid_email:
            errormassage = "You allrady have an account "
            return render(request, 'Jberry/signup.html', {'error': errormassage})

        else:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)

            user.save()
            errormassage = "Account created success fully "
            return render(request, 'Jberry/signup.html', {'error': errormassage})
