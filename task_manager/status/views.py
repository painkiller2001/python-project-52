from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.status.forms import StatusForm
from task_manager.status.models import Status


class StatusesView(LoginRequiredMixin, ListView):
    
    model = Status
    template_name = 'status/statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):

    model = Status
    form_class = StatusForm
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан')
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, 'Статус уже существует')
        return super().form_invalid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Status
    form_class = StatusForm
    template_name = 'status/status_update.html'
    success_url = reverse_lazy('statuses')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно изменен')
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):

    model = Status
    template_name = 'status/delete_confirmation.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        if self.object.tasks.exists():
            messages.error(self.request, 'Невозможно удалить статус')
            return redirect(self.success_url)
        messages.success(self.request, 'Статус успешно удален')
        return super().form_valid(form)