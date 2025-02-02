from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, email_verification, password_recovery

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='/home/webcam/course_work_django/users/templates/users/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path("password_recovery/", password_recovery, name='password_recovery'),
]
