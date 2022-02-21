from rest_framework import serializers
from category.models import Category
from store.serializers import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "get_absolute_url", "owner", 'products')
