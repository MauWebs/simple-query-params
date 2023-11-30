
from django.urls import path

from .views import *

urlpatterns = [
    path('get/all/', product_list, name='product-list'),
    path('post/', product_create, name='product-create'),
]