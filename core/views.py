from core.models import User
from core.serializers import UserCreateSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['password']) < 8:
            return 'Password is too short'
        if request.data['password'] != request.data['password_repeat']:
            return 'Password mismatch'
        return self.create(request, *args, **kwargs)


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# class UserViewSet(ModelViewSet):
#     dsfs
