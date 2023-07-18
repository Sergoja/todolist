from core import views
from core.views import UserDetailView, UserUpdateView, UserDeleteView, UserCreateView, UserLoginView
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('profile/', UserDetailView.as_view()),
    path('profile/', UserUpdateView.as_view()),
    path('profile/', UserDeleteView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('signup/', UserCreateView.as_view()),
    # path('update_password/', put, patch),
]
