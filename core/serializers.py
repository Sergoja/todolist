from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.models import User
from rest_framework import serializers, status
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(ModelSerializer):
    password_repeat = serializers.CharField(max_length=128, required=True)

    def save(self, *args, **kwargs):
        user = User(username=self.validated_data['username'])

        password = self.validated_data['password']
        password_repeat = self.validated_data['password_repeat']

        validate_password(password)

        if password != password_repeat:

            raise serializers.ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["username", "password", "password_repeat"]


class UserUpdateSerializer(ModelSerializer):

    # def edit_password(self, request):
    #     if request.method == 'PATCH':
    #         if request.data['old_password'] != request.data['password']:
    #             return Response("Not correct password", status=status.HTTP_404_NOT_FOUND)
    #         user = request.user
    #         if request.data['new_password'] is not None:
    #             user.set_password(request.data['new_password'])
    #             user.save()
    #         else:
    #             return Response("New password is None", status=status.HTTP_404_NOT_FOUND)

    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(ModelSerializer):
    def login_user(self, request):
        if request.method == "POST":
            username = request.POST['username'],
            password = request.body['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

