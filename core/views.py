from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import User
from core.permissions import IsOwner, IsStaff
from core.serializers import UserSerializer, UserListSerializer, UserCreateUpdateSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, ListAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    default_permission = [IsAuthenticated, IsOwner | IsStaff]

    def auth(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("invalid login", status=status.HTTP_401_UNAUTHORIZED)


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

    def auth(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("invalid login", status=status.HTTP_401_UNAUTHORIZED)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def auth(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("invalid login", status=status.HTTP_401_UNAUTHORIZED)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def auth(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("invalid login", status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
