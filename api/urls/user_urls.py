from api.views.user_views import UserRegistrationAPIView, MyTokenObtainPairView
from django.urls import path

urlpatterns = [
    path("login", MyTokenObtainPairView.as_view(), name="login"),
    path("register", UserRegistrationAPIView.as_view(), name="register"),

]