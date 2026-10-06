from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        raise Exception("Test error for SDK")
        return render(
            request,
            'index.html',
            context={
                'name': 'Valerik'
            }
        )