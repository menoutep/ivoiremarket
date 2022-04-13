from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Categories, SousCategories, Tags, Marques, Images, Caracteristiques,Products, Order, Cart
from accounts.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields=('username','role')

class CategoriesAdmin(admin.ModelAdmin):
    search_fields=('name',)
   
class MarquesAdmin(admin.ModelAdmin):
    search_fields=('name',)
    
class ImagesAdmin(admin.ModelAdmin):
    search_fields=('name',)
    
class TagsAdmin(admin.ModelAdmin):
    search_fields=('name',)
    
class SousCategoriesAdmin(admin.ModelAdmin):
    search_fields=('name',)
    
class CaracteristiquesAdmin(admin.ModelAdmin):
    search_fields=('name',)

class ProductsAdmin(admin.ModelAdmin):
    search_fields=('name','seller')

class OrderAdmin(admin.ModelAdmin):
    search_fields=('product','user',)
    
class CartAdmin(admin.ModelAdmin):
    search_fields=('user',)

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Marques, MarquesAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(SousCategories, SousCategoriesAdmin)
admin.site.register(Caracteristiques, CaracteristiquesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)