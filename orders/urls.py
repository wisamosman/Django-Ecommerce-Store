from django.urls import path
from .views import add_to_cart, OrderList,chackout_page
from .api import CartDetailCreateDeleteAPI, OrderDetailAPI , OrderListAPI , CreateOrderAPI


app_name = "orders"

urlpatterns = [
    path('' , OrderList.as_view()),
    path('add-to-cart' , add_to_cart ,name='add_to_cart'),
    path('checkout' , chackout_page),
    # api
    path('api/<str:username>/cart' , CartDetailCreateDeleteAPI.as_view()),
    path('api/<str:username>/cart/create-order' , CreateOrderAPI.as_view()),

    path('api/<str:username>/orders' , OrderListAPI.as_view()),
    path('api/<str:username>/orders/<int:pk>' , OrderDetailAPI.as_view()),
]