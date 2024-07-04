from django.contrib import admin
from .models import *

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'agent_firstname')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('data_supply', 'supplier')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer_firstname', 'buyer_name', 'buyer_surname', 'delivery_address', 'date_create')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'create_date')

@admin.register(Pos_parametr)
class Pos_parametrAdmin(admin.ModelAdmin):
    list_display = ('product', 'parametr', 'value')

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'count')

@admin.register(Pos_supply)
class Pos_supplyAdmin(admin.ModelAdmin):
    list_display = ('product', 'supply', 'count')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('location', 'capacity')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name', 'rating')
