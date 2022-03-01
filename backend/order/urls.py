from .views import OrderItemViewSet, OrderViewSet
from django.urls import include, path
from backend.SharedAPIRootRouter import SharedAPIRootRouter

router = SharedAPIRootRouter()
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'order_items',OrderItemViewSet, basename="order_items")
