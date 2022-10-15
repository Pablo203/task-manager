from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainPage, name="index"),
    path('tasksList/', views.tasksKanban, name='tasksKanban'),
    path('tasksList/addTask', views.addTask, name='addTask'),
    path('tasksList/addTaskExecute', views.addTaskExecute, name='addTaskExecute'),

    path('tasksList/taskDetail/<int:taskId>/', views.taskDetail, name='taskDetail'),
]