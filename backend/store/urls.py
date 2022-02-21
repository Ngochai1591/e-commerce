from django.urls import include, path
from backend.SharedAPIRootRouter import SharedAPIRootRouter

from .views import ProductViewSet

router = SharedAPIRootRouter()
router.register(r'products', ProductViewSet, basename="products")
