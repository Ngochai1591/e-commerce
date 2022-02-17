from unicodedata import category
from categories.models import Category
from categories.serializers import  CategorySerializer
from backend.permissions import IsStaffOrReadOnly

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class CategoryList(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
    
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = CategorySerializer(data=request.data)
#         print("USER", request.user.is_staff)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CategoryDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsStaffOrReadOnly]

#     def get_object(self, pk):
#         try:
#             category  = Category.objects.get(pk=pk)
#             return category
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self,request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
