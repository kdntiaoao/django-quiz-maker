from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import View

from .models import Quiz


class IndexView(View):
    def get(self, request, *args, **kwargs):
        quizzes = Quiz.objects.select_related("created_by").all()
        return TemplateResponse(request, "quizzes/index.html", {"quizzes": quizzes})


index = IndexView.as_view()


class ThinkingView(View):
    def get(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        return TemplateResponse(request, "quizzes/thinking.html", {"quiz": quiz})


thinking = ThinkingView.as_view()


class ResultView(View):
    def get(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        return TemplateResponse(request, "quizzes/result.html", {"quiz": quiz})


result = ResultView.as_view()
