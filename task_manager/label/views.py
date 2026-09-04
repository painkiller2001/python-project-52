from django.shortcuts import render, redirect
from django.views import View
from task_manager.label.forms import LabelForm
from django.contrib import messages
from task_manager.label.models import Label

# Create your views here.
class LabelsView(View):

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(
            request,
            "label/labels.html",
            context={
                'labels': labels
            }
        )


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(
            request,
            'label/label_create.html',
            context={
                'form': form
            }
        )
        

    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, 'Метка успешно создана')
            return redirect('labels')
        else:
            message = messages.warning(request, 'Метка уже существует')
        return render(
            request,
            'label/label_create.html',
            context={
                'form': form
            }
        )


class LabelUpdateView(View):

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id') 
        label = Label.objects.get(id=label_id)
        form = LabelForm(instance=label)
        return render(
            request,
            'label/label_create.html',
            context={
                'label': label,
                'form': form
            }
        )


    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            message = messages.success(request, 'Метка успешно обновлена')
            return redirect('labels')
        return render(
            request,
            'label/label_update.html',
            context={
                'labels': label,
                'form': form
            }
        )   


class LabelDeleteView(View):

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        return render(
            request,
            'label/delete_confirmation.html',
            context={
                'label': label
            }
        )


    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        if label:
            label.delete()
            messages.success(request, 'Метка успешно удалена')
            return redirect('labels')
        return render(
            request,
            "label/delete_confirmation.html",
            context={
                'label': label
            }
        )
