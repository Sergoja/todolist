from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import User
from core.permissions import IsOwner, IsStaff
from core.serializers import UserSerializer, UserListSerializer, \
    UserCreateSerializer, UserUpdateSerializer, LoginSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

    def post(self, *args, **kwargs):
        user = User(username=self.request.data['username'])

        password = self.request.data['password']
        password_repeat = self.request.data['password_repeat']

        validate_password(password)

        if password != password_repeat:
            raise ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()

        return Response(status=status.HTTP_200_OK)



class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])

        return JsonResponse({
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_staff": user.is_staff,
            "is_active": user.is_active,
            "date_joined": user.date_joined,
            "last_login": user.last_login,
            "role": user.role
        })


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

    def put(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])

        user.username = request.data["username"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.email = request.data["email"]

        user.save()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

    def patch(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        pass


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


