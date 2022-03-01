from xmlrpc.client import ResponseError
from rest_framework import serializers, status
from .models import Cart, CartItem
from store.serializers import ProductSerializer
from accounts.serializers import AccountSerializer
from rest_framework.response import Response


class CartSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    items = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Cart
        fields = ('id', 'owner', 'created_at','updated_at', 'items')

    def create(self, validated_data):
        #Check relation between owner and cart is existed or not
        owner = validated_data.get('owner')
        error = {"message":"This user has already owned cart"}
        
        # #first way
        # if not Cart.objects.filter(owner=owner).exists():
        #     cart = Cart.objects.create(owner=owner)
        #     return cart
        # else:
        #     raise serializers.ValidationError(error)
        
        # second way
        cart, is_created = Cart.objects.get_or_create(owner=owner)
        if is_created:
            return cart
        else:
            raise serializers.ValidationError(error)


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')

