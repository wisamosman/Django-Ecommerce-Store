from .models import Cart





def get_cart_data(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user,completed=False)
        return {'cart_data':cart}

    else:
        return {}