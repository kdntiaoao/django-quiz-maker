from django.contrib import admin
from django.urls import include, path
from django.http.response import HttpResponse


def top(request):
    return HttpResponse("top")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", top),
    path("accounts/", include("accounts.urls")),
    # path('quizzes/', include('quizzes.urls'))
]
