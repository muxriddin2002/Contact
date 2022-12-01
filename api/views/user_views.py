from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime
from api.serializers.user_serializers import UserRegistrationSerializer, UserSerializerWithToken, UserSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class UserRegistrationAPIView(ListCreateAPIView):
    serializer_class = UserRegistrationSerializer






class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #
    #     # Add custom claims
    #     token['name'] = user.username
    #     token['key'] = 'val'
    #     # ...
    #
    #     return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        self.user.last_login = datetime.now()
        self.user.save()
        # del data['refresh']
        print(serializer)
        for key, val in serializer.items():
            print(key, "->>", val)
            data[key] = val

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
