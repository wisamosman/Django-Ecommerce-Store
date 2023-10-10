from rest_framework import generics
from rest_framework.response import Response
from .models import Cart , CartDetail , Order , OrderDetail
from .serializers import CartDetailSerializer , CartSerializer
from django.contrib.auth.models import User


class CartDetailCreateDeleteAPI(generics.GenericAPIView):
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,completed=False)
        data = CartSerializer(cart).data
        return Response({'Cart':data , 'Status':200})


    def post(self,request,*args, **kwargs):
        pass


    def delete(self,request,*args, **kwargs):
        pass