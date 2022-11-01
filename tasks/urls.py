from django.urls import path
#from . import views 
from .views import views
from .views import apiViews
from .views import filesViews


urlpatterns = [
    path('', views.mainPage, name="index"),
    
    path('tasksList/getTasks/', apiViews.getAll, name='getTasks'),
    
    path('tasksList/<int:projectId>/', views.tasksKanban, name='tasksKanban'),

    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/', views.taskDetail, name='taskDetail'),

    path('taskList<int:projectId>/taskDetail/<int:taskId>/taskStateChange/', views.taskStateChange, name='taskStateChange'),

    path('taskList/<int:projectId>/taskDetail/<int:taskId>/deleteTask/', views.deleteTask, name='deleteTask'),

    

    path('tasksList/<int:projectId>/addTask/', views.addTask, name='addTask'),
    path('tasksList/<int:projectId>/addTaskExecute/', views.addTaskExecute, name='addTaskExecute'),

    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/upload/', filesViews.uploadFile, name='uploadFile')
]