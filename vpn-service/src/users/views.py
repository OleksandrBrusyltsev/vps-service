from django.shortcuts import render
from rest_framework.generics import UpdateAPIView

from serizalizer import ProfileUserModel, ProfileSerializer


# Create your views here.
class UserProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileUserModel.objects.all()

    def get_object(self):
        return self.request.user.profile
