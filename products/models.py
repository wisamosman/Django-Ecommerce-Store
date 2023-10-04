from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=30000)
    sku = models.IntegerField()
    price = models.FloatField()


class ProductImages(models.Model):
    pass


class Brand(models.Model):
    pass



class Review(models.Model):
    pass