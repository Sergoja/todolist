from core import views
from core.views import UserCreateView, UserLoginView, UserRetrieveUpdateDestroyView, UserUpdateView
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('profile', UserRetrieveUpdateDestroyView.as_view()),
    path('login', UserLoginView.as_view()),
    path('signup', UserCreateView.as_view()),
    path('update_password', UserUpdateView.as_view()),
]
