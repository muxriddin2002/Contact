from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["is_superuser", "is_active", "groups", "user_permissions", 'last_login', 'date_joined']
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", 'username', 'first_name', 'last_name', 'last_login']


class UserSerializerWithToken(serializers.ModelSerializer):
    #token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

    # def get_token(self, obj):
    #     token = RefreshToken.for_user(obj)
    #     return str(token.access_token)
