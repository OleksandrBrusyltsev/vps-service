from django.db import models

from users.models import User

from websites.models import UserCreatedSite


# Create your models here.
class VPNAccessStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(UserCreatedSite, on_delete=models.CASCADE)
    visits = models.PositiveIntegerField(default=0)
    data_sent = models.FloatField(default=0)
    data_received = models.FloatField(default=0)
    # Додайте інші поля, які вам потрібні для статистики

    def __str__(self):
        return f"Stats for {self.user.username} on {self.site.name}"