from django import forms

class TaskCreateForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    shortDescription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    longDescription = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))

    category = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    CHOICES = (
    ('toDo', 'To do'),
    ('inProgress', 'In progress'),
    ('done', 'Done'),
    )
    state = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'class': 'form-control'}))
    priority = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #projectName = forms.CharField()

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ProjectCreateForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))