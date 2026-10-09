from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from task_manager.status.forms import StatusForm
from task_manager.status.models import Status


class StatusesView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            "status/statuses.html",
            context={
                'statuses': statuses
            }
        )


class StatusCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(
            request,
            'status/status_create.html',
            context={
            'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect(
                'statuses'
            )
        else:
            messages.warning(request, 'уже существует')
        return render(
            request,
            'status/status_create.html',
            context={
            'form': form
            }
        )


class StatusUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request,
            'status/status_update.html',
            context={
                'status': status,
                'form': form 
            }
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно изменен')
            return redirect(
                'statuses'
            )
        return render(
            request,
            'status/status_update.html',
            context={
                'status': status,
                'form': form
            }
        )   


class StatusDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id) 
        return render(
            request,
            'status/delete_confirmation.html',
            context={
                'status': status
            }
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status.objects.all(), id=status_id)

        if status.tasks.exists(): 
            messages.error(request, 'Невозможно удалить статус')
            return redirect('statuses') 
        else:
            status.delete()
            messages.success(request, 'Статус успешно удален')
            return redirect('statuses')