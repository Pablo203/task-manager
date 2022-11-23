from django.urls import path
from . import views 

urlpatterns = [
     path('<int:projectId>/<int:taskId>/upload/', views.uploadFile, name='uploadFile'),
    path('<int:projectId>/<int:taskId>/<str:fileName>/fileConfirm/', views.deleteFileConfirm, name='deleteFileConfirm'),
    path('<int:projectId>/<int:taskId>/<str:fileName>/fileDelete/', views.deleteFile, name="deleteFile"),
    path('filesList/', views.showFiles, name='showFiles'),
]