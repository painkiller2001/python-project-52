"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager.task.views import TasksView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path("create/", TaskCreateView.as_view(), name='task_create'),
    path("<int:id>/", TaskUpdateView.as_view(), name='task_update'),
    path("<int:id>/update/", TaskUpdateView.as_view(), name='task_update'),
    path("<int:id>/delete/", TaskDeleteView.as_view(), name='task_delete'),
]
