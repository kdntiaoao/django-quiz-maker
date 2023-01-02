from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ResisterView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("register")


register = ResisterView.as_view()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("login")


login = LoginView.as_view()
