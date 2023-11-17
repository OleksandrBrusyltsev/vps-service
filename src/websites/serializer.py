from rest_framework.serializers import ModelSerializer

from websites.models import UserCreatedSite


class UserCreatedSiteSerializer(ModelSerializer):
    class Meta:
        model = UserCreatedSite
        fields = ('id', 'user', 'site_name', 'site_url', 'proxied_url')  # Додайте інші поля за потребою