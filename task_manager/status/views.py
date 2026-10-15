from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from task_manager.status.forms import StatusForm
from task_manager.status.models import Status


# class StatusesView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         statuses = Status.objects.all()
#         return render(
#             request,
#             "status/statuses.html",
#             context={
#                 'statuses': statuses
#             }
#         )
class StatusesView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/statuses.html'
    context_object_name = 'statuses'


# class StatusCreateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         form = StatusForm()
#         return render(
#             request,
#             'status/status_create.html',
#             context={
#             'form': form
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         form = StatusForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Статус успешно создан')
#             return redirect(
#                 'statuses'
#             )
#         else:
#             messages.warning(request, 'уже существует')
#         return render(
#             request,
#             'status/status_create.html',
#             context={
#             'form': form
#             }
#         )
class StatusCreateView(LoginRequiredMixin, CreateView):

    model = Status
    form_class = StatusForm
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан')
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, 'Стутус уже существует')
        return super().form_invalid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Status
    form_class = StatusForm
    template_name = 'status/status_update.html'
    success_url = reverse_lazy('statuses')
    id_url = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно изменен')
        return super().form_valid(form)
# class StatusUpdateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         status_id = kwargs.get('id')
#         status = Status.objects.get(id=status_id)
#         form = StatusForm(instance=status)
#         return render(
#             request,
#             'status/status_update.html',
#             context={
#                 'status': status,
#                 'form': form 
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         status_id = kwargs.get('id')
#         status = Status.objects.get(id=status_id)
#         form = StatusForm(request.POST, instance=status)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Статус успешно изменен')
#             return redirect(
#                 'statuses'
#             )
#         return render(
#             request,
#             'status/status_update.html',
#             context={
#                 'status': status,
#                 'form': form
#             }
#         )   


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