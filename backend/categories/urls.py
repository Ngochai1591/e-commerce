# from categories.views import CategoryDetail, CategoryList
# urlpatterns = [
#     path('categories/', CategoryList.as_view()),
#     path('categories/<int:pk>/', CategoryDetail.as_view())
# ]

# from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path, include
# from categories.views import CategoryViewSet
# from django.urls import path

# category_list = CategoryViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# category_detail = CategoryViewSet.as_view({
#     'get':'retreive',
#     'put':'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = format_suffix_patterns([ 
#     path(r'categories/', category_list, name='category-list'),
#     path(r'categories/<int:pk>/', category_detail, name='category-detail')
# ])


from categories.views import CategoryViewSet
# from rest_framework.routers import DefaultRouter
from django.urls import path, include
from backend.SharedAPIRootRouter import SharedAPIRootRouter

#Create router
router = SharedAPIRootRouter()
router.register(r'categories', CategoryViewSet, basename='categories')

# urlpatterns = [path('', include(router.urls))]