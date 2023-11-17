from django.contrib import admin
from .models import User, ProfileUser
from statistics_site.models import VPNAccessStats
from websites.models import UserCreatedSite

admin.site.register(User)
admin.site.register(ProfileUser)
admin.site.register(UserCreatedSite)
admin.site.register(VPNAccessStats)