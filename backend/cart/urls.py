from .views import CartViewSet, CartItemViewSet
from django.urls import include, path
from backend.SharedAPIRootRouter import SharedAPIRootRouter

router = SharedAPIRootRouter()
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'cart_items',CartItemViewSet, basename="cart_items")
