from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import Account
from rest_framework_simplejwt.views import TokenObtainPairView
from cart.views import CartViewSet

from .serializers import RegisterSerializer, MyCustomObtainPairSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
        
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as err:
            print("ERR", err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MyCustomObtainPairView(TokenObtainPairView):
    serializer_class = MyCustomObtainPairSerializer