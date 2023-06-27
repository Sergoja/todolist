from core.views import UserCreateView, Logout
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('<int:pk>', UserViewSet.as_view())
]

router = routers.SimpleRouter()
# router.register('', core.views.UserViewSet)
urlpatterns += router.urls
