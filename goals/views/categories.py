from django.db import transaction
from rest_framework.response import Response
from rest_framework import permissions, filters, status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination

from core.models import User
from goals.models import GoalCategory, Goal
from goals.permission import GoalCategoryPermission
from goals.serializers import GoalCategorySerializer, GoalCategoryWithUserSerializer


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer



class GoalCategoryListView(ListAPIView):
    serializer_class = GoalCategoryWithUserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["tittle", "created"]
    ordering = ["tittle"]
    search_fields = ["tittle"]

    def get_queryset(self):
        return GoalCategory.objects.filter(
            user_id=self.request.user.id,
            is_deleted=False
        )


class GoalCategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCategoryWithUserSerializer

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.goal_set.update(status=Goal.status.archived)
