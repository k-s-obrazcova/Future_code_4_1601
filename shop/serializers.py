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
