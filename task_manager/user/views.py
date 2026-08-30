from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from task_manager.user.models import User
from task_manager.user.forms import UserForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
# Create your views here.


class UsersView(View):
    
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
            "user/user_create.html",
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        else:
            messages.warning(request, 'уже существует')
        return render(
            request,
            "user/user_create.html",
            context={
                'form': form
            }
        )

    
# class LoginView(View):
    
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             "user/login.html",
#             context={
#                 "login": ...,
#             },
#         )


class CustomLogoutView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "user/logout_confirmation.html",
            context={
            }
        )

    def post(self, request, *args, **kwargs):

        logout(request)
        messages.success(request, 'Вы разлогинены')
        return redirect('index')


class UpdateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        current_user_id = request.user.id

        if current_user_id == user_id:
            form = UserForm(instance=user)
            return render(
                request,
                "user/user_update.html",
                context={
                    'form': form,
                    'user': user
                }
            )
        else:
            messages.error(request, 'У вас нет прав для изменения')
            return redirect('users')

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users')
        return render(
            request,
            "user/user_update.html",
            context={
                'form': form,
                'user': user
            }
        )


class DeleteView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        current_user_id = request.user.id

        if current_user_id == user_id:
            return render(
                request,
                "user/delete_confirmation.html",
                context={
                    'user': user
                }
            )
        else:
            messages.error(request, 'У вас нет прав для изменения')
            return redirect('users')

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            messages.success(request, 'Пользователь успешно удален')
            return redirect('users')
        return render(
            request,
            "user/delete_confirmation.html",
            context={
                'user': user
            }
        )