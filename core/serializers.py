from core.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
