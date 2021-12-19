from django.urls import path
from home.views.index import Index
from home.views.signup import Signup

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view(), name='signup'),
]
