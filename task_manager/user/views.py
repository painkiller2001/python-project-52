from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.user.forms import UserForm
from task_manager.user.models import User

# Create your views here.


# class UsersView(View):
    
#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         return render(
#             request,
#             "user/users.html",
#             context={
#                 "users": users
#             }
#         )
class UsersView(ListView):

    model = User
    template_name = 'user/users.html'
    context_object_name = 'users'


class UserCreateView(CreateView):

    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    
    model = User
    form_class = UserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        user_id = kwargs.get('id')
        current_user_id = request.user.id
        if current_user_id != user_id:
            messages.error(request, 'У вас нет прав для изменения')
            return redirect('users')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно изменен')
        return super().form_valid(form)


# class UserCreateView(View):
    
#     def get(self, request, *args, **kwargs):
#         form = UserForm()
#         return render(
#             request,
#             "user/user_create.html",
#             context={
#                 'form': form
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно зарегистрирован')
#             return redirect('login')
#         return render(
#             request,
#             "user/user_create.html",
#             context={
#                 'form': form
#             }
#         )

    
class CustomLoginView(View):
    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "user/login.html",
            context={
            }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вы залогинены')
            return redirect('index')
        else:
            messages.warning(request, 'Вы ввели неверный логин и пароль')
            return render(
                request, 
                "user/login.html", 
                context={'username': username}
            )

        
class CustomLogoutView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        logout(request)
        messages.success(request, 'Вы разлогинены')
        return redirect('index')


# class UserUpdateView(LoginRequiredMixin, View):
    
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get('id')
#         user = User.objects.get(id=user_id)
#         current_user_id = request.user.id

#         if current_user_id == user_id:
#             form = UserForm(instance=user)
#             return render(
#                 request,
#                 "user/user_update.html",
#                 context={
#                     'form': form,
#                     'user': user
#                 }
#             )
#         else:
#             messages.error(request, 'У вас нет прав для изменения')
#             return redirect('users')

#     def post(self, request, *args, **kwargs):
#         user_id = kwargs.get('id')
#         user = User.objects.get(id=user_id)
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно изменен')
#             return redirect('users')
#         return render(
#             request,
#             "user/user_update.html",
#             context={
#                 'form': form,
#                 'user': user
#             }
#         )


# class UserDeleteView(LoginRequiredMixin, View):
    
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get('id')
#         user = User.objects.get(id=user_id)
#         current_user_id = request.user.id

#         if current_user_id == user_id:
#             return render(
#                 request,
#                 "user/delete_confirmation.html",
#                 context={
#                     'user': user
#                 }
#             )
#         else:
#             messages.error(request, 'У вас нет прав для изменения')
#             return redirect('users')

#     def post(self, request, *args, **kwargs):
#         user_id = kwargs.get('id')
#         user = User.objects.get(id=user_id)
#         if user.created_tasks.exists() or user.assigned_tasks.exists(): 
#             messages.error(request, 'Невозможно удалить пользователя')
#             return redirect('users')
#         else:
#             user.delete()
#             messages.success(request, 'Пользователь успешно удален')
#             return redirect('users')


class UserDeleteView(LoginRequiredMixin, DeleteView):

    model = User
    template_name = 'user/delete_confirmation.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('users')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        user_id = kwargs.get('id')
        current_user_id = request.user.id
        if current_user_id != user_id:
            messages.error(request, 'У вас нет прав для изменения')
            return redirect('users')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.object.created_tasks.exists() or self.object.assigned_tasks.exists():
            messages.error(self.request, 'Невозможно удалить пользователя')
            return redirect('users')
        messages.success(self.request, 'Пользователь успешно удален')
        return super().form_valid(form)