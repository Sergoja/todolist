from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from goals.filters import GoalDateFilter
from goals.models import Goal
from goals.permission import GoalPermission
from goals.serializers import GoalSerializer, GoalWithUserSerializer


class GoalCreateView(CreateAPIView):
    serializer_class = GoalSerializer


class GoalListView(ListAPIView):
    serializer_class = GoalWithUserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Goal.objects.filter(
            category__board__participants__user_id=self.request.user.id,
            category__is_deleted=False
        ).exclude(status=Goal.status.archived)


class GoalDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalWithUserSerializer

    def get_queryset(self):
        return Goal.objects.filter(
            user=self.request.user, is_deleted=False,
            category__is_deleted=False
        ).exclude(status=Goal.status.archived)

    def perform_destroy(self, instance):
        instance.status = Goal.status.archived
        instance.save()

