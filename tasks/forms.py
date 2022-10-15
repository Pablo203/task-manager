from django import forms

class TaskCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    shortDescription = forms.CharField(max_length=100)
    longDescription = forms.CharField(max_length=500)

    category = forms.CharField(max_length=50)

    CHOICES = (
    ('toDo', 'To do'),
    ('inProgress', 'In progress'),
    ('done', 'Done'),
    )
    state = forms.CharField(widget=forms.Select(choices=CHOICES))
    # state = forms.CharField()
    priority = forms.IntegerField()