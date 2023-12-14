from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class ProductAdmin2(TranslationOptions):
    # inlines = (TranslationTabularInline, )
    # list_display = ['id','name']
    fields = ('name', 'description')




translator.register(Product,ProductAdmin2)