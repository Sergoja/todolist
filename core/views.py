from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import User
from core.permissions import IsOwner, IsStaff
from core.serializers import UserSerializer, UserListSerializer, UserCreateUpdateSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['password']) < 8:
            return 'Password is too short'
        if request.data['password'] != request.data['password_repeat']:
            return 'Password mismatch'
        return self.create(request, *args, **kwargs)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserLoginView(LoginView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer


