from django.contrib import admin
from django.urls import include, path
from django.template.response import TemplateResponse


def top(request):
    return TemplateResponse(request, "quizzes/top.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", top),
    path("accounts/", include("accounts.urls")),
    # path('quizzes/', include('quizzes.urls'))
]
