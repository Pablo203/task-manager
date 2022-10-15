from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import is_valid_path
from .models import Task
from .forms import TaskCreateForm

# Create your views here.
def mainPage(request):
    return render(request, 'index.html', {})

def tasksKanban(request):   
    toDoTasks = Task.objects.filter(state="toDo").order_by("-priority")
    inProgressTasks = Task.objects.filter(state="inProgress").order_by("-priority")
    doneTasks = Task.objects.filter(state="done").order_by("-priority")


    return render(request, 'tasks.html', {'toDoTasks': toDoTasks, 'inProgressTasks': inProgressTasks, 'doneTasks': doneTasks})

def taskDetail(request, taskId):
    task = Task.objects.get(id=taskId)
    return render(request, 'taskDetail.html', {'task': task})

def addTaskExecute(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            task = Task(
                name=form.cleaned_data['name'], shortDescription=form.cleaned_data['shortDescription'], 
                longDescription=form.cleaned_data['longDescription'], 
                category=form.cleaned_data['category'],
                state=form.cleaned_data['state'],
                priority=form.cleaned_data['priority'],
                )
            task.save()
            return HttpResponse("FORM WORKS")
    else:
        form = TaskCreateForm()
    
    return render(request, 'addTaskForm.html', {'form': form})

def addTask(request):
    form = TaskCreateForm()
    return render(request, 'addTaskForm.html', {'form': form})