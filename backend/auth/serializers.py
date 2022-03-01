from rest_framework import serializers
from accounts.models import Account
from cart.models import Cart


class RegisterSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('username','password','password2', 'email', 'first_name', 'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
        
    def create(self, validated_data):
        del validated_data['password2']

        user = Account.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        cart, is_created = Cart.objects.get_or_create(owner=user)
        if is_created:
            print("Create new cart for this user")
        else:
            print("Get cart for this user")

        return user
        
#Create customer token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyCustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        #Add custome claims
        token['username'] = user.username
        token['is_staff'] = user.is_staff

        return token
