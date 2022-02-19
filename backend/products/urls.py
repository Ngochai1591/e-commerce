
# from rest_framework.urlpatterns import format_suffix_patterns

# from django.urls import path
# from products.views import ProductViewSet

# product_list  = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# product_detail = ProductViewSet.as_view({
#     'get': 'retrive',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = format_suffix_patterns([
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
# ])

# from rest_framework.routers import DefaultRouter
from django.urls import path, include
from backend.SharedAPIRootRouter import SharedAPIRootRouter

from products.views import ProductViewSet

#Create router
router = SharedAPIRootRouter()
router.register(r'products', ProductViewSet, basename="products")

# urlpatterns = [path('', include(router.urls))
# ]