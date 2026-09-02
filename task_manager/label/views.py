from django.shortcuts import render
from django.views import View
from task_manager.label.forms import LabelForm

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
        ...


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