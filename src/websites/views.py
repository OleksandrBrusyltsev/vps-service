from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from websites.models import UserCreatedSite
from websites.serializer import UserCreatedSiteSerializer


# Create your views here.
class UserCreatedSiteDetail(generics.RetrieveAPIView):
    queryset = UserCreatedSite.objects.all()
    serializer_class = UserCreatedSiteSerializer
    lookup_field = 'id'  # Ідентифікатор для пошуку деталей конкретного сайту

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized_data = self.get_serializer(instance).data

        # Заміна посилань на внутрішній роутинг тут, у serialized_data
        user_site_name = instance.site_name  # Отримання назви сайту
        routes_on_original_site = "http://127.0.0.1:8000/"

        # Заміна посилань у серіалізованих даних
        processed_data = self.process_serialized_data(serialized_data, user_site_name, routes_on_original_site)

        return Response(processed_data)

    def process_serialized_data(self, serialized_data, user_site_name, routes_on_original_site):
        # Отримання серіалізованих даних
        # Процес заміни посилань у serialized_data тут

        # Приклад: заміна посилань у полях site_url у serialized_data
        for data in serialized_data:
            if 'site_url' in data:
                data['site_url'] = f'localhos/{user_site_name}/{routes_on_original_site}'
                # Замініть 'site_url' на власний ключ поля, яке ви хочете замінити

        return serialized_data