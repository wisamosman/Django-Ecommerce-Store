from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from .models import Product,ProductImages,Brand,Review


class ProductAdmin2(TranslationAdmin):
    # inlines = (TranslationTabularInline, )
    list_display = ['id','name']
    # fields = ('name', 'description')
    # only_current_lang = ('description', )
    # inlines = (TranslationStackedInline, )

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

#class ProductAdmin(SummernoteModelAdmin):
    #list_display = ['name','price','brand','flag']
    #list_filter = ['price','tags','brand','flag']
    #search_fields = ['name','subtitle','description']
    #inlines = [ProductImagesAdmin,]
    #summernote_fields = '__all__'


admin.site.register(Product,ProductAdmin2)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)