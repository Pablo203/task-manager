from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Project, Task, File
from .forms import UploadFileForm

# Create your tests here.
class UrlsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test123!')
        self.project = Project.objects.create(name="Test")
        self.task = Task.objects.create(
            name = "Test",
            description = "Test",
            category = "Test",
            state = "toDo",
            priority = 1,
            createdBy = self.user,
            projectName = self.project
        )

        

    def test_dashboard_view(self):
        self.client.login(username='test', password='test123!')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_kanban_view(self):
        self.client.login(username='test', password='test123!')
        response = self.client.get(reverse('tasksKanban', kwargs={'projectId': self.project.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks.html')
    
    def test_task_view(self):
        self.client.login(username='test', password='test123!')
        response = self.client.get(reverse('taskDetail', kwargs={   
            'projectId': self.project.id,
            'taskId': self.task.id,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskDetail.html')