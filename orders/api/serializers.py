
from rest_framework import serializers

from orders.models import Order,OrderItem,Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'