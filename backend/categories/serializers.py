
from rest_framework import serializers
from categories.models import Category
from products.serializers import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "get_absolute_url", "owner", 'products')
