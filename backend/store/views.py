from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.permissions import IsStaffOrReadOnly
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['GET'], detail=False, name="Get Latest Product")
    def lastest_product(self, request, *args, **kwargs):
        lastest_4_products = Product.objects.all()[0:3]
        serializer = ProductSerializer(lastest_4_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
