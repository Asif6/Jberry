from django.urls import path
from home.views.index import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
