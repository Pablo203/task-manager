from django.urls import path
#from . import views 
from .views import views
from .views import apiViews
from .views import filesViews


urlpatterns = [
    path('', views.mainPage, name="index"),

    path('tasksList/addProject/', views.addProject, name='addProject'),
    path('tasksList/addProjectExecute/', views.addProjectExecute, name='addProjectExecute'),
    #path('tasksList/<int:projectId>/deleteProject/', views.deleteProject, name='deleteProject'),

    path('tasksList/<int:projectId>/', views.tasksKanban, name='tasksKanban'),
    path('tasksList/<int:projectId>/addTask/', views.addTask, name='addTask'),
    path('tasksList/<int:projectId>/addTaskExecute/', views.addTaskExecute, name='addTaskExecute'),
    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/', views.taskDetail, name='taskDetail'),
    path('taskList<int:projectId>/taskDetail/<int:taskId>/taskStateChange/', views.taskStateChange, name='taskStateChange'),
    path('taskList/<int:projectId>/taskDetail/<int:taskId>/editTask/', views.editTask, name='editTask'),
    path('taskList/<int:projectId>/taskDetail/<int:taskId>/editTaskExecute/', views.editTaskExecute, name='editTaskExecute'),

    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/taskConfirm/', views.deleteTaskConfirm, name='deleteTaskConfirm'),
    path('taskList/<int:projectId>/taskDetail/<int:taskId>/deleteTask/', views.deleteTask, name='deleteTask'),

    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/upload/', filesViews.uploadFile, name='uploadFile'),
    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/<str:fileName>/fileConfirm/', views.deleteFileConfirm, name='deleteFileConfirm'),
    path('tasksList/<int:projectId>/taskDetail/<int:taskId>/<str:fileName>/fileDelete/', filesViews.deleteFile, name="deleteFile"),

    path('tasksList/getTasks/', apiViews.getAll, name='getTasks'),
    path('tasksList/<int:taskId>/<str:state>/changeState/', apiViews.changeState, name='changeState'),
]