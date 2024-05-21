from django.contrib import admin
from django.urls import path, include
from Tasks import views

app_name = 'Tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('task_create', views.task_create, name='task-create'),
    path('task_list/<int:show_done>', views.task_list, name='task-list'),
    path('task_update/<int:pk>', views.task_update, name='task-update'),
    path('task_delete/<int:pk>', views.task_delete, name='task-delete'),
    path('aboth', views.about_page, name='about-page'),
]
