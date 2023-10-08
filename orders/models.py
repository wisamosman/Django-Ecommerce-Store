from django.db import models
from django.utils import timezone
from accounts.models import Address
from products.models import Product
from django.contrib.auth.models import User
from utils.generate_code import generate_code

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,blank=True,null=True)
    code = models.CharField(max_length=30,default=generate_code)
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default='Recieved')
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_location = models.ForeignKey(Address,related_name='delivery_address',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.code




class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='order_product',on_delete=models.SET_NULL,null=True)
    price = models.FloatField
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,blank=True,null=True)
    completed = models.BooleanField(default=False)

     # instance method
    def cart_total(self):
        total = 0
        for product in self.cart_detail.all():
            total += product.total
        return total



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='cart_product',on_delete=models.SET_NULL,null=True)
    price = models.FloatField
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)



class Coupon(models.Model):
    code = models.CharField(max_length=25)
    percentage = models.FloatField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()

    def __str__(self):
        return self.code