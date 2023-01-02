from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "quizzes"
urlpatterns = [
    path("<int:quiz_id>/thinking", views.thinking, name="thinking"),
    path("<int:quiz_id>/result/", views.result, name="result"),
]
