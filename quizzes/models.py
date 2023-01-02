from django.conf import settings
from django.db import models


class Quiz(models.Model):
    statement = models.TextField("問題文")
    option1 = models.CharField("選択肢1", max_length=150)
    option2 = models.CharField("選択肢2", max_length=150)
    option3 = models.CharField("選択肢3", max_length=150)
    option4 = models.CharField("選択肢4", max_length=150)
    option5 = models.CharField("選択肢5", max_length=150)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="作成者", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.statement
