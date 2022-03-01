from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from backend.permissions import IsStaffOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    

# Create your views here.
