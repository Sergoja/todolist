from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from core.models import User
from core.serializers import UserCreateSerializer, UserLoginSerializer, \
    UserRetrieveUpdateDestroySerializer, UserUpdateSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


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
        user.last_name = self.request.data['last_name']
        user.first_name = self.request.data['first_name']
        user.email = self.request.data['email']
        
        try:
            user.save()
        except Exception:
            return Response("Такой пользователь уже существует", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroySerializer

    def get(self, request, *args, **kwargs):
        user = get_user(request)

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

    def put(self, request, *args, **kwargs):
        user = get_user(request)

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
        user = get_user(request)
        pass

    def delete(self, request, *args, **kwargs):
        logout(request)

        return Response(status=status.HTTP_200_OK)


class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

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
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserUpdateView(UpdateAPIView):
    serializer_class = UserUpdateSerializer

    def patch(self, request, *args, **kwargs):
        user = get_user(request)

        old_password = request.data['old_password']
        new_password = request.data['new_password']

        check_password = user.check_password(old_password)

        if check_password is not True:
            return Response('Неправильный пароль', status=status.HTTP_404_NOT_FOUND)

        validate_password(new_password)

        user.set_password(request.data['new_password'])
        user.save()

        return Response(status=status.HTTP_200_OK)

