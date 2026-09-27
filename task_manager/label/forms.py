from django import forms

from task_manager.label.models import Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']