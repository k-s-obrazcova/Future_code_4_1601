from rest_framework import serializers
from .models import *


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['name', 'description', 'price', 'size', 'color', 'create_date', 'update_date', 'is_exists',
                  'developer']


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['buyer_name', 'buyer_firstname', 'comment', 'building_time_start', 'building_time_finish', 'key_time',
                  'realtor']


class DevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Development
        fields = '__all__'


class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosOrder
        fields = ['house', 'order', 'count', 'discount']


class PosDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosDevelopment
        fields = ['house', 'development', 'count']
