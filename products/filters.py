from django_filters import rest_framework as filters

from .models import Product
from django import forms 
import django_filters

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name' : ['contains'] , 
            'price':['range','lte','gte'],
            'flag':['exact'],
        }