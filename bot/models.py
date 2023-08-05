from django.db import models

from core.models import User


# class TgUser(models.Model):
#     chat_id = models.IntegerField(max_length=20)
#     user_ud = models.IntegerField(max_length=20)
#     user_id = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)
