from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.label.forms import LabelForm
from task_manager.label.models import Label


# Create your views here.
class LabelsView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/labels.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):

    model = Label
    form_class = LabelForm
    template_name = 'label/label_create.html'
    success_url = reverse_lazy('labels')

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно создана')
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, 'Метка уже существует')
        return super().form_invalid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Label
    form_class = LabelForm
    template_name = 'label/label_update.html'
    success_url = reverse_lazy('labels')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно изменена')
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):

    model = Label
    template_name = 'label/delete_confirmation.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('labels')

    def form_valid(self, form):
        if self.object.assigned_labels.exists():
            messages.error(self.request, 'Невозможно удалить метку')
            return redirect(self.success_url)
        messages.success(self.request, 'Метка успешно удалена')
        return super().form_valid(form)