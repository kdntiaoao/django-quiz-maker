from django.template.response import TemplateResponse
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "quizzes/index.html", {})


index = IndexView.as_view()


class ThinkingView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "quizzes/thinking.html", {})


thinking = ThinkingView.as_view()


class ResultView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "quizzes/result.html", {})


result = ResultView.as_view()
