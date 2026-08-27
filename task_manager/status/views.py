from django.shortcuts import render
from django.views import View
from task_manager.status.models import Status

# Create your views here.
class StatusesView(View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            "status/statuses.html",
            context={
                'statuses': statuses
            }
        )