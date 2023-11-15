from django.db import transaction
from rest_framework.serializers import ModelSerializer

from .models import User, ProfileUserModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileUserModel
        fields = ('id',
                  'name',
                  'surname',
                  'age',
                  'avatar')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "dob",
            "user_type",
            "phone_number",
            "is_active",
            "created_at",
            "updated_at",
            "profile_picture",
        )
        extra_kwargs = {"password": {"write_only": True}}


    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')

        user = User.objects.create_user(**validated_data)

        ProfileUserModel.objects.create(**profile, user=user)

        return user
