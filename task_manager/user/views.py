from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from task_manager.user.models import User
from task_manager.user.forms import UserForm
# Create your views here.


class UserView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(
            request,
            "user/users.html",
            context={
                "users": users
            }
        )
        

class CreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(
            request,
            "user/create.html",
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(
            request,
            "user/create.html",
            context={
                'form': form
            }
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


class UpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(
            request,
            "user/user_update.html",
            context={
                'form': form,
                'user': user
            }
        )


    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(
            request,
            "user/user_update.html",
            context={
                'form': form,
                'user': user
            }
        )


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...