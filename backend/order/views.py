from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import action

from backend.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from accounts.models import Account

from django.db.models import F, Sum, FloatField

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint that allows orders to be viewed or created

    Args:
        viewsets (_type_): _description_
    """    

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Add info and perform checks before saving an Order

        Before creating an Order, there is a check on the customer's cart items.
        If the cart item quantity causes the product's available inventory to
        dip below zero, a validation error is raised.If there is enough inventory to support the order, an Order is created
        and cart items are used to make order items. After that the cart is
        cleared.

        NOTE: Cart items are not deleted. When the cart is cleared the cart items
        still exist but are disassociated from the cart. The cart is empty so
        that the user can add new things to it, but cart items are preserved as
        they could be helpful in drawing insights from customer behavior or making
        suggestions. For example, what they have put in their cart previously,
        what other similar products might she/he like, etc.

        Args:
            serializer (OrderSerialiazer): Serialized representation of Order we are creating
        
        """

        try:
            owner = self.request.user
        except Exception as err:
            print("[ERROR] ", err)        
            raise serializers.ValidationError("User was not found")
        
        cart = owner.cart

        #Check each cart_item and product.stock 
        for cart_item in cart.items.all():
            if cart_item.product.is_available and (cart_item.product.stock - cart_item.quantity <=0):
                raise serializers.ValidationError(
                    'We do not have enough inventory of ' + str(cart_item.product.name) + ' to complete your purchase. Sorry, we will restock soon'
                )
        
        #find the order total using the quantity of each cart item and product's price
        total_aggregated_dict = cart.items.aggregate(total=Sum(F('quantity')*F('product__price'), output_field=FloatField()))

        order_total = round(total_aggregated_dict['total'], 2)
        order = serializer.save(owner=owner,total=order_total)

        order_items = []
        for cart_item in cart.items.all():
            order_items.append(OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity))
            #stock should decrement by the appropriate amount
            cart_item.product.stock -= cart_item.quantity
            if cart_item.product.stock == 0:
                cart_item.product.is_available = False
            cart_item.product.save()
        
        #bulk_create for create multiple objects
        OrderItem.objects.bulk_create(order_items)
        # use clear instead of delete since it removes all objects from the
        # related object set. It doesnot delete the related objects it just
        # disassociates them, which is what we want in order to empty the cart
        # but keep cart items in the db for customer data analysis
        cart.items.clear()

    def create(self, request, *args, **kwargs):
        """Override the creation of Order objects.

        Args:
            request (dict): _description_
        """        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print("HEADERS",headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], url_path='order_history/(?P<owner_id>[0-9])', detail=False)
    def order_history(self, request, owner_id):
        """Return a list of a user's orders

        Args:
            request (request): _description_
            owner_id (integer): _description_
        """

        try:
            owner = Account.objects.get(pk=owner_id)
        except Exception as err:
            print('[ERROR]', err)
            return Response({'status':'fail'})
        
        orders =  Order.objects.filter(owner=owner)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

class OrderItemViewSet(viewsets.ModelViewSet):
    """API endpoint that allows order items to be viewed or edited

    Args:
        viewsets (_type_): _description_
    """    

    permission_classes =[IsAuthenticatedOrReadOnly]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
