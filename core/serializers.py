from core.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


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

