from django.db import transaction
from rest_framework.serializers import ModelSerializer

from .models import User, ProfileUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "is_active",
            "created_at",
            "updated_at",

        )
        extra_kwargs = {"password": {"write_only": True}}


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id', 'name', 'surname', 'age', 'avatar')