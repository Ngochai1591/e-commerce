from .models import Order, OrderItem
from rest_framework import serializers
from accounts.serializers import AccountSerializer

class OrderSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    order_items = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Order
        fields = 