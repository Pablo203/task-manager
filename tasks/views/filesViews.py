from ..models import Task, Project
from files.models import File
from ..forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
#from django.core.mail import send_mail

def handle_uploaded_file(request, f, taskId):
    name = f.name
    task = Task.objects.get(id=taskId)
    
    with open('G:\getFiles\%s' % name, 'ab') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    file = File(
        name = name,
        createdBy = request.user,
        originTask = task,
        localisation = 'G:\getFiles\%s' % name,
    )
    file.save()

def uploadFile(request, projectId, taskId):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request, request.FILES['file'], taskId)
            # send_mail(
            #     'Django test',
            #     'Django message',
            #     'taskManager@test.com',
            #     ['pawelrosa686@gmail.com'],
            #     fail_silently=False,
            #     )
            return HttpResponseRedirect(reverse('taskDetail', kwargs={'projectId': projectId, 'taskId': taskId}))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'projectId': projectId})

def deleteFile(request, projectId, taskId, fileName):
    file = File.objects.get(name=fileName, originTask=taskId)
    file.delete()

    return HttpResponseRedirect(reverse('taskDetail', kwargs={'projectId': projectId, 'taskId': taskId}))

@user_passes_test(lambda u: u.groups.filter(name='FilesManager').exists(), login_url='index')
def showFiles(request):
    user = request.user
    projects = Project.objects.filter(createdBy=request.user)
    tasks = Task.objects.filter(createdBy=request.user)
    files = File.objects.all()
    return  render(request, 'filesManage.html', {'projects' : projects, 'tasks': tasks, 'user': user})