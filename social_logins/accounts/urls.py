from django.urls import path
from accounts import views

urlpatterns = [
    path('v1/google/login', views.GoogleLogin.as_view(), name='google_login'),
]
