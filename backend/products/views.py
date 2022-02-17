# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.permissions import IsStaffOrReadOnly

from rest_framework.viewsets import ViewSet

from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(ViewSet):
    queryset=  Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# class ProductList(APIView):
#     permission_classes = [IsStaffOrReadOnly, IsAuthenticatedOrReadOnly]
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductDetail(APIView):
#     permission_classes = [IsStaffOrReadOnly, IsAuthenticatedOrReadOnly]
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

    