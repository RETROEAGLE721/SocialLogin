from django.urls import path
from accounts import views

urlpatterns = [
    path('v1/login', views.Login.as_view(), name='login'),
]
