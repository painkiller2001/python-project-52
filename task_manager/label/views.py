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
        ...


    def post(self, request, *args, **kwargs):
        ...


class LabelDeleteView(View):

    def get(self, request, *args, **kwargs):
        ...


    def post(self, request, *args, **kwargs):
        ...