from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView
from .models import Order, Cart , CartDetail
from products.models import Product


class OrderList(ListView):
    model = Order


def add_to_cart(request):

    # get data frontend 
    product = Product.objects.get(id=request.POST['product_id'])
    qauntity = request.POST['quantity']

    # get cart
    cart = Cart.objects.get(user=request.user,completed=False)

    # cart detail 
    cart_detail  , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    cart_detail.quantity = qauntity
    cart_detail.price = product.price
    cart_detail.total = round(int(qauntity) * product.price,2)
    cart_detail.save()

    return redirect(f'/products/{product.slug}')
    # # cart detail 
    # cart_detail  , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    # if created : 
    #     cart_detail.quantity = qauntity
    # else:
    #     cart_detail.quantity += qauntity

    # cart_detail.price = product.price
    # cart_detail.total = int(qauntity) * product.price
    # cart_detail.save()