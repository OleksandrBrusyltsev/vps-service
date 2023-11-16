from django.urls import path


from users_auth.views import AuthRegisterView

from users_auth.views import LoginView

urlpatterns = [

    path('register/', AuthRegisterView.as_view(), name='auth_register'),
    path("login/", LoginView.as_view(), name="auth_login"),

]