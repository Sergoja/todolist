from django.urls import path

from goals.views.board import BoardCreateView, BoardListView, BoardView
from goals.views.categories import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryDetailView
from goals.views.comments import GoalCommentCreateView, GoalCommentListView, GoalCommentDetailView
from goals.views.goal import GoalCreateView, GoalListView, GoalDetailView

urlpatterns = [
    path("goal_category/create", GoalCategoryCreateView.as_view()),
    path("goal_category/list", GoalCategoryListView.as_view()),
    path("goal_category/<int:pk>", GoalCategoryDetailView.as_view()),
    path("goal/create", GoalCreateView.as_view()),
    path("goal/list", GoalListView.as_view()),
    path("goal/<int:pk>", GoalDetailView.as_view()),
    path("goal_comment/create/", GoalCommentCreateView.as_view()),
    path("goal_comment/list", GoalCommentListView.as_view()),
    path("goal_comment/<int:pk>", GoalCommentDetailView.as_view()),
    path('board/create', BoardCreateView.as_view(), name='create-board'),
    path('board/list', BoardListView.as_view(), name='board-list'),
    path('board/<int:pk>', BoardView.as_view(), name='board'),
]