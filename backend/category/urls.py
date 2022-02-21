import django


from django.urls import path, include
from backend.SharedAPIRootRouter import SharedAPIRootRouter
from .views import CategoryViewSet

router = SharedAPIRootRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
