from django.shortcuts import render
from products.models import Product , Brand , Review


def home(request):
    brands = Brand.objects.all()
    sale_products = Product.objects.filter(flag='Sale')
    feature_products = Product.objects.filter(flag='Feature')
    new_products = Product.objects.filter(flag='New')
    reviews = Review.objects.all()

    return render(request,'settings/home.html',{
        'brands':brands , 
        'sale_products':sale_products,
        'feature_products':feature_products,
        'new_products':new_products,
        'reviews':reviews,

    })