from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task'),
    path('task-detail/<int:task_id>/', views.task_detail , name='task-detail'),
    path('task-create', views.create_task , name='create-task'),
    path('task/update/<int:task_id>/',views.update_task , name='task-update'),
    path('delete-task/<int:task_id>/' , views.delete_task , name='delete-task')
]
