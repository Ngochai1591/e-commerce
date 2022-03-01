from django.urls import path
from auth.views import RegisterView, MyCustomObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns =[
    path('login/', MyCustomObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]