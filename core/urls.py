from core import views
from core.views import UserDeleteView, UserCreateView, LoginView, UserRetrieveUpdateView
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('profile/', UserRetrieveUpdateView.as_view()),
    path('profile/', UserDeleteView.as_view()),
    path('login/', LoginView.as_view()),
    path('signup/', UserCreateView.as_view()),
    # path('update_password/', put, patch),
]
