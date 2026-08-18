from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "user/create.html",
            context={
                "create": ...,
            },
        )

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "user/login.html",
            context={
                "login": ...,
            },
        )