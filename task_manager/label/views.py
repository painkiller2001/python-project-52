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



# class LabelsView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         labels = Label.objects.all()
#         return render(
#             request,
#             "label/labels.html",
#             context={
#                 'labels': labels
#             }
#         )


# class LabelCreateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         form = LabelForm()
#         return render(
#             request,
#             'label/label_create.html',
#             context={
#                 'form': form
#             }
#         )
        

#     def post(self, request, *args, **kwargs):
#         form = LabelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Метка успешно создана')
#             return redirect('labels')
#         else:
#             messages.warning(request, 'Метка уже существует')
#         return render(
#             request,
#             'label/label_create.html',
#             context={
#                 'form': form
#             }
#         )


# class LabelUpdateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         label_id = kwargs.get('id') 
#         label = Label.objects.get(id=label_id)
#         form = LabelForm(instance=label)
#         return render(
#             request,
#             'label/label_update.html',
#             context={
#                 'label': label,
#                 'form': form
#             }
#         )


#     def post(self, request, *args, **kwargs):
#         label_id = kwargs.get('id')
#         label = Label.objects.get(id=label_id)
#         form = LabelForm(request.POST, instance=label)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Метка успешно изменена')
#             return redirect('labels')
#         return render(
#             request,
#             'label/label_update.html',
#             context={
#                 'labels': label,
#                 'form': form
#             }
#         )   


# class LabelDeleteView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         label_id = kwargs.get('id')
#         label = Label.objects.get(id=label_id) 
#         return render(
#             request,
#             'label/delete_confirmation.html',
#             context={
#                 'label': label
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         label_id = kwargs.get('id')
#         label = Label.objects.get(id=label_id)
        
#         if label.assigned_labels.exists():
#             messages.error(request, 'Невозможно удалить метку')
#             return redirect('labels') 
#         else:
#             label.delete()
#             messages.success(request, 'Метка успешно удалена')
#             return redirect('labels')

