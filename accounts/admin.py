from django.contrib import admin

# Register your models here.
# from django.contrib.auth.admin import UserAdmin
from .models import Profile , Phones , Address
# from django.contrib.auth.models import User


# class MyUser(UserAdmin):
#     pass





class PhonesAdmin(admin.TabularInline):
    model = Phones

class AddressAdmin(admin.TabularInline):
    model = Address


class ProfileAdmin(admin.ModelAdmin):
    # inlines = [PhonesAdmin,AddressAdmin]
    pass




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Phones)
admin.site.register(Address)
# admin.site.register(User,MyUser)