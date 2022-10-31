from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ..models import Task
from ..forms import TaskCreateForm, UploadFileForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required


# Create your views here.
def mainPage(request):
    return render(request, 'index.html', {})

@login_required
def tasksKanban(request):
    currentUser = request.user
    toDoTasks = Task.objects.filter(state="toDo", createdBy=currentUser).order_by("-priority")
    inProgressTasks = Task.objects.filter(state="inProgress", createdBy=currentUser).order_by("-priority")
    doneTasks = Task.objects.filter(state="done", createdBy=currentUser).order_by("-priority")
    return render(request, 'tasks.html', {'toDoTasks': toDoTasks, 'inProgressTasks': inProgressTasks, 'doneTasks': doneTasks})

@login_required
def taskDetail(request, taskId):
    task = Task.objects.get(id=taskId)
    form = UploadFileForm()
    return render(request, 'taskDetail.html', {'task': task, 'form': form})

@login_required
def addTaskExecute(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            currentUser = request.user
            #currentUserId = currentUser.id
            task = Task(
                name=form.cleaned_data['name'], shortDescription=form.cleaned_data['shortDescription'], 
                longDescription=form.cleaned_data['longDescription'], 
                category=form.cleaned_data['category'],
                state=form.cleaned_data['state'],
                priority=form.cleaned_data['priority'],
                createdBy=currentUser
                )
            task.save()
            return HttpResponseRedirect(reverse('tasksKanban'))
    else:
        form = TaskCreateForm()
    
    return render(request, 'addTaskForm.html', {'form': form})

def addTask(request):
    form = TaskCreateForm()
    return render(request, 'addTaskForm.html', {'form': form})

def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)
    task.delete()
    return HttpResponseRedirect(reverse('tasksKanban'))

def taskStateChange(request, taskId):
    task = Task.objects.get(id=taskId)
    if task.state == 'toDo':
        task.state = 'inProgress'
    elif task.state == 'inProgress':
        task.state = 'done'
    task.save()

    return HttpResponseRedirect(reverse('tasksKanban'))

