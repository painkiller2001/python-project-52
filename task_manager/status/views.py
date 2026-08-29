from django.shortcuts import render, redirect
from django.views import View
from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
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
            'status/create.html',
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
            'status/create.html',
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
        form = StatusForm(instance=status)
        return render(
            request,
            'status/delete_confirmation.html',
            context={
                'status': status,
                'form': form 
            }
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
            messages.success(request, 'Статус успешно удален')
            return redirect('statuses')
        return render(
            request,
            "status/delete_confirmation.html",
            context={
                'status': status
            }
        )