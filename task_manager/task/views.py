from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.task.forms import TaskFilterForm, TaskForm
from task_manager.task.models import Task


# Create your views here.
class TasksView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'task/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = super().get_queryset()
        params = {
            'status_id': self.request.GET.get('status'),
            'performer_id': self.request.GET.get('performer'),
            'labels__id': self.request.GET.get('label')
        }
        params = {k: v for k, v in params.items() if v}
        filtered_tasks = tasks.filter(**params)

        flag = self.request.GET.get('own_tasks')
        if flag:
            own_filtered_tasks = filtered_tasks.filter(author=self.request.user)
        else:
            own_filtered_tasks = filtered_tasks
        return own_filtered_tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = 'task/task_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Задача успешно создана')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Задача уже существует')
        return super().form_invalid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Задача успешно изменена')
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):

    model = Task
    template_name = 'task/delete_confirmation.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        current_user_id = request.user.id
        if current_user_id != task.author.id:
            messages.error(request, 'Задачу может удалить только ее автор')
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Задача успешно удалена')
        return super().form_valid(form)