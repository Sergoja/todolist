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
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    password_repeat = serializers.CharField(max_length=128, required=True)
    last_name = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password", "password_repeat"]


class UserRetrieveUpdateDestroySerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "old_password", "new_password"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

