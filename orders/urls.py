from django.urls import path
from .views import add_to_cart, OrderList
from .api import CartDetailCreateDeleteAPI


app_name = "orders"

urlpatterns = [
    path('' , OrderList.as_view()),
    path('add-to-cart' , add_to_cart),
    # api
    path('api/<str:username>/cart' , CartDetailCreateDeleteAPI.as_view()),
]