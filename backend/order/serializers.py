from itertools import product
from .models import Order, OrderItem
from rest_framework import serializers
from accounts.serializers import AccountSerializer

from store.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order Model

    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
    """    
    owner = AccountSerializer(read_only=True)
    order_items = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Order
        fields = (
            'id', 'owner', 'total', 'created_at', 'updated_at', 'order_items'
        )

    def create(self, validated_data):
        """Override the creation of Order objects

        Args:
            validated_data (dict): _description_
        """        
        order = Order.objects.create(**validated_data)
        return order

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for Order Item Model

    Args:
        serializers (_type_): _description_
    """    
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            'id','order','product','quantity'
        )