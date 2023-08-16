from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from goals.filters import GoalDateFilter
from goals.models import Goal, GoalComment
from goals.permission import GoalPermission, GoalCommentPermission
from goals.serializers import GoalCommentSerializer, GoalCommentCreateSerializer


class GoalCommentCreateView(CreateAPIView):
    serializer_class = GoalCommentCreateSerializer


class GoalCommentListView(ListAPIView):
    serializer_class = GoalCommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ["goal"]
    ordering = ["-created"]

    def get_queryset(self):
        return GoalComment.objects.filter(
            goal__category__board__participants__user_id=self.request.user.id
        )


class GoalCommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCommentSerializer

    def get_queryset(self):
        return GoalComment.objects.select_related('user').filter(user_id=self.request.user.id)
