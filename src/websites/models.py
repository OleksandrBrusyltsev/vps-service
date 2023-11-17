from django.db import models

from users.models import User


# Create your models here.
class UserCreatedSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)  # Назва сайту
    site_url = models.URLField()  # URL сайту

    def str(self):
        return f"Site created by {self.user.username}: {self.site_name}"