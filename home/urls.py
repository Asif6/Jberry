from django.urls import path
from home.views.index import Index
from home.views.signup import Signup
from home.views.login import Login, Logout

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view(), name='signup'),
    path("login/", Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]
