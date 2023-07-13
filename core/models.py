from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class UserRoles(TextChoices):
    USER = "member", "Пользователь"
    ADMIN = "admin", "Админ"


class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
