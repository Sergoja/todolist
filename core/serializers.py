from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.response import Response

from core.models import User
from rest_framework import serializers, status
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password


class UserCreateUpdateSerializer(ModelSerializer):
    # old_password = serializers.CharField(max_length=128, required=False)
    # new_password = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

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

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


@csrf_exempt
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

