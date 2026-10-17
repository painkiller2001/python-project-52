from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from task_manager.task.forms import TaskFilterForm, TaskForm
from task_manager.task.models import Task


# Create your views here.
class TasksView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        form = TaskFilterForm(request.GET)
        params = {
            'status_id': request.GET.get('status'),
            'performer_id': request.GET.get('performer'),
            'labels__id': request.GET.get('label')
        }
        params = {k: v for k, v in params.items() if v}
        filtered_tasks = tasks.filter(**params)

        flag = request.GET.get('own_tasks')
        if flag:
            own_filtered_tasks = filtered_tasks.filter(author=request.user)
        else:
            own_filtered_tasks = filtered_tasks

        
        return render(
            request,
            'task/tasks.html',
            context={
                'tasks': own_filtered_tasks,
                'form': form
            }
        )


class TaskDetailView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = get_object_or_404(Task, id=task_id)
        return render(
            request,
            'task/task_detail.html',
            context={
                'task': task
            }
        )


# class TaskCreateView(LoginRequiredMixin, View): 

#     def get(self, request, *args, **kwargs):
#         form = TaskForm()
#         return render(
#             request,
#             'task/task_create.html',
#             context={
#                 'form': form
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.author = request.user
#             form.save()
#             messages.success(request, 'Задача успешно создана')
#             return redirect(
#                 'tasks'
#             )
#         else:
#             messages.warning(request, 'Задача уже существует')
#         return render(
#             request,
#             'task/task_create.html',
#             context={
#                 'form': form
#             }
#         )          
    


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


# class TaskUpdateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         task_id = kwargs.get('id') 
#         task = Task.objects.get(id=task_id)
#         form = TaskForm(instance=task)

#         return render(
#             request,
#             'task/task_update.html',
#             context={
#                 'task': task,
#                 'form': form
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         task_id = kwargs.get('id') 
#         task = Task.objects.get(id=task_id)
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Задача успешно изменена')
#             return redirect(
#                 'tasks'
#             )
#         return render (
#             request,
#             'task/task_update.html',
#             context={
#                 'task': task,
#                 'form': form
#             }
#         )


class TaskUpdateView(LoginRequiredMixin, UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Задача успешно изменена')
        return super().form_valid(form)


# class TaskDeleteView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         task_id = kwargs.get('id')
#         task = Task.objects.get(id=task_id)
#         current_user_id = request.user.id
#         if current_user_id != task.author.id:
#             messages.error(request, 'Задачу может удалить только ее автор')
#             return redirect('tasks')

#         return render (
#                 request,
#                 'task/delete_confirmation.html',
#                 context={
#                     'task': task
#                 }
#             )


#     def post(self, request, *args, **kwargs):
#         task_id = kwargs.get('id') 
#         task = Task.objects.get(id=task_id)
#         current_user_id = request.user.id
#         if current_user_id != task.author.id:
#             messages.error(request, 'Задачу может удалить только ее автор')
#             return redirect('tasks')
#         else:
#             task.delete()
#             messages.success(request, 'Задача успешно удалена')
#             return redirect('tasks')


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