from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Product
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from backend.permissions import IsOwnerOrReadOnly

# Create your views here.
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['PUT', 'POST'], detail=True, name="add to cart")
    def add_to_cart(self, request, pk=None):
        """Add an item to a user's cart.

        Adding to cart is disallowed if there is not enough inventory for the
        product available. If there is, the quantity is increased on an existing
        cart item or a new cart item is created with that quantity and added
        to the cart.

        Args:
            request (_type_): request
            pk (_type_, optional): _description_. Defaults to None.

        Return the updated cart
        """        

        cart = self.get_object()
        try:
            product = Product.objects.get(pk=request.data['product_id'])
            quantity = int(request.data['quantity'])
        except Exception as err:
            print("[ERROR_add_to_cart] " ,err)
            return Response(data={'status':'fail'}, status=status.HTTP_400_BAD_REQUEST)
        
        #disallow adding to cart if stock is not enough
        if product.stock <= 0 or product.stock - quantity < 0:
            print("[INFO] There is no more product avaiable")
            return Response({'status':'fail'})
        
        #Check Item  is existing in cart or not, If Existed, increase quantity
        existing_cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if existing_cart_item:
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            new_cart_item.save()
        
        #return updated cart
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST','PUT'], detail=True, name="remove items from cart")
    def remove_from_cart(self, request, pk=None):
        """Remove an item from user's cart
        If current quantity less than 1, delete cart_item
        else decrease quantity by 1 

        Args:
            request (_type_): _description_
            pk (_type_, optional): _description_. Defaults to None.
        """        

        cart = self.get_object()
        try:
            product = Product.objects.get(pk=request.data['product_id'])
        except Exception as err:
            print('[ERROR_remove_from_cart] ', err)
            return Response({'status': 'fail'} , status=status.HTTP_400_BAD_REQUEST)
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except Exception as err:
            print('[ERROR_remove_from_cart] ', err)
            return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)
        
        #If quantity is 1, remove cartitem
        #Else decrease quantity
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
        
        #return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

