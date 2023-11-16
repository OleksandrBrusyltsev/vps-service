from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

from users.serizalizer import UserSerializer


class UserSignUpSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = True
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """
    Serializer for obtaining and validating user tokens.
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data
