from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from goals.models import GoalCategory, Goal, GoalComment


class GoalCategoryPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalCategory):
        return request.user == obj.user


class GoalPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Goal):
        return request.user == obj.user


class GoalCommentPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalComment):
        return request.user == obj.user
