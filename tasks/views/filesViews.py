from ..models import Task, File
from ..forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        localisation = 'G:\getFiles\%s' % name
    )
    file.save()

def uploadFile(request, projectId, taskId):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request, request.FILES['file'], taskId)
            return HttpResponseRedirect(reverse('taskDetail', kwargs={'projectId': projectId, 'taskId': taskId}))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'projectId': projectId})