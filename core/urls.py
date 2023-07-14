from core.views import UserCreateView, Logout, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', UserListView.as_view()),
    path('profile/<int:pk>', UserDetailView.as_view()),
    path('profile/create/', UserCreateView.as_view()),
    path('profile/<int:pk>/update/', UserUpdateView.as_view()),
    path('profile/<int:pk>/delete/', UserDeleteView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
