from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.views import View


class ResisterView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "accounts/register.html")


register = ResisterView.as_view()


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"


login = LoginView.as_view()
