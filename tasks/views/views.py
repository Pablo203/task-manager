from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ..models import Task, Project
from ..forms import TaskCreateForm, UploadFileForm, ProjectCreateForm
from django.contrib.auth.decorators import login_required
from files.models import File


# Create your views here.
@login_required
def mainPage(request):
    user = request.user
    projects = Project.objects.filter(createdBy=request.user)
    tasks = Task.objects.filter(createdBy=request.user)
    

    return render(request, 'index.html', {'projects' : projects, 'tasks': tasks, 'user': user})

@login_required
def tasksKanban(request, projectId):
    currentUser = request.user
    projects = Project.objects.filter(createdBy=request.user)

    toDoTasks = Task.objects.filter(state="toDo", createdBy=currentUser, projectId=projectId).order_by("-priority")
    inProgressTasks = Task.objects.filter(state="inProgress", createdBy=currentUser, projectId=projectId).order_by("-priority")
    doneTasks = Task.objects.filter(state="done", createdBy=currentUser, projectId=projectId).order_by("-priority")
    
    return render(request, 'tasks.html', {'toDoTasks': toDoTasks, 'inProgressTasks': inProgressTasks, 'doneTasks': doneTasks, 'projectId': projectId, 'projects' : projects})

@login_required
def taskDetail(request, projectId, taskId):
    projects = Project.objects.filter(createdBy=request.user)
    
    task = Task.objects.get(id=taskId)
    files = File.objects.filter(originTask=taskId)
    form = UploadFileForm()
    return render(request, 'taskDetail.html', {'task': task, 'form': form, 'projectId': projectId, 'projects' : projects, 'files': files})

@login_required
def addTaskExecute(request, projectId):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            currentUser = request.user
            currentProject = Project.objects.get(id=projectId)
            task = Task(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'], 
                category=form.cleaned_data['category'],
                state=form.cleaned_data['state'],
                priority=form.cleaned_data['priority'],
                createdBy=currentUser,
                projectName = currentProject,
                projectId = currentProject.id
                )
            task.save()
            return HttpResponseRedirect(reverse('tasksKanban', kwargs={'projectId': projectId}))
    else:
        form = TaskCreateForm()
    
    return render(request, 'addTaskForm.html', {'form': form})

def addProjectExecute(request):
    if request.method == "POST":
        form = ProjectCreateForm(request.POST)

        if form.is_valid():
            currentUser = request.user
            project = Project(
                name=form.cleaned_data['name'],
                createdBy = currentUser
                )
            project.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ProjectCreateForm()
    
    return render(request, 'addProjectForm.html', {'form': form})


def addTask(request, projectId):
    form = TaskCreateForm()
    return render(request, 'addTaskForm.html', {'form': form, 'projectId': projectId})

@login_required
def addProject(request):
    form = ProjectCreateForm()
    return render(request, 'addProjectForm.html', {'form': form})

def deleteTask(request, projectId, taskId):
    task = Task.objects.get(id=taskId)
    task.delete()
    return HttpResponseRedirect(reverse('tasksKanban', kwargs={'projectId': projectId}))

def editTask(request, projectId, taskId):
    #project = Project.objects.get(id=projectId)
    task = Task.objects.get(id=taskId)
    form = TaskCreateForm(initial={
        'name': task.name,
        'description': task.description,
        'category': task.category,
        'state': task.state,
        'priority': task.priority,
    })
    return render(request, 'editTask.html', {'form': form, 'projectId': projectId, 'taskId': taskId})

def editTaskExecute(request, projectId, taskId):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        task = Task.objects.get(id=taskId)
        if form.is_valid():
            task.name = form.cleaned_data['name']
            task.description = form.cleaned_data['description']
            task.category = form.cleaned_data['category']
            task.state = form.cleaned_data['state']
            task.priority = form.cleaned_data['priority']
            task.save()
    return HttpResponseRedirect(reverse('taskDetail', kwargs={'projectId': projectId, 'taskId': taskId}))
    



def taskStateChange(request, projectId, taskId):
    task = Task.objects.get(id=taskId)
    if task.state == 'toDo':
        task.state = 'inProgress'
    elif task.state == 'inProgress':
        task.state = 'done'
    task.save()

    return HttpResponseRedirect(reverse('tasksKanban', kwargs={'projectId': projectId}))

def deleteTaskConfirm(request, projectId, taskId):
    projects = Project.objects.filter(createdBy=request.user)
    project = Project.objects.get(id=projectId)
    task = Task.objects.get(id=taskId)

    return render(request, 'deleteTaskConfirm.html', {'project': project, 'task': task, 'projects': projects})


    