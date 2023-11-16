from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import ProfileUser
from users.serizalizer import ProfileSerializer


# Create your views here.
class UserProfileUpdateView(UpdateAPIView , CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileUser.objects.all()

    def get_object(self):
        return self.request.user.profile


