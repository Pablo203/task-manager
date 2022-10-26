from ..models import Task
from ..forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponse

def handle_uploaded_file(f, taskId):
    name = f.name
    task = Task.objects.get(id=taskId)
    with open('G:\getFiles\%s' % name, 'ab') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    task = Task.objects.get(id=taskId)
    task.filePath += task.filePath + ' G:\getFiles\%s' % name
    task.save()

def uploadFile(request, taskId):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], taskId)
            return HttpResponse("SUCCESS")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})