
from django.urls import path

from .views.productindex import Productindex

urlpatterns = [
    path("", Productindex.as_view(), name='productindex')
]
