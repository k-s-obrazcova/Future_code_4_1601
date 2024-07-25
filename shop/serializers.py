from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_name',
            'buyer_firstname',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'product'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'create_date',
            'update_date',
            'photo',
            'exists',
            'category',
            'tag',
            'warehouse',
            'parametr'

        ]


class ProductSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = [
            'data_supply',
            'supplier',
            'product'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description'
        ]


class ParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]


class Pos_parametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_parametr
        fields = [
            'product',
            'parametr',
            'value'
        ]


class Pos_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'product',
            'order',
            'count',
            'discount'
        ]


class Pos_supplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_supply
        fields = [
            'product',
            'supply',
            'count'
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'manager',
            'location',
            'capacity'
        ]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'product',
            'warehouse',
            'quantity'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'product',
            'user_name',
            'rating',
            'comment'
        ]
