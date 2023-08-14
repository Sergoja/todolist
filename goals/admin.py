from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("tittle", "user", "created", "updated")
    search_fields = ("tittle", "user")


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("tittle", "user", "category")
    search_fields = ("tittle", "user", "description")


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("text", "user", "goal")
    search_fields = ("text", "user")


