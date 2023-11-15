from django.urls import path

from users.views import UserProfileUpdateView

urlpatterns = [

    path('/profile', UserProfileUpdateView.as_view(), name='users_profile_update'),

]