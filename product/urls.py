
from unicodedata import name
from django.urls import path

from .views.productindex import Productindex
from .views.trending import Trending
from .views.product_by_category import Product_by_category
from .views.product_details import Product_details


urlpatterns = [
    path("", Productindex.as_view(), name='productindex'),
    path('trending/',Trending.as_view(),name='trending'),
    path('product/<cat>',Product_by_category.as_view(),name='catproduct'),
    path('products_details/<int:id>',Product_details.as_view(),name='products_details'),
    
    
]
