from django.forms import ModelForm, Select

from .models import *
from django.forms import ModelForm, Textarea, TextInput, DateInput, SelectMultiple, CheckboxInput


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['header', 'description']
        widgets = {
            'header': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),

        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['header', 'description', 'deadline', 'members']
        widgets = {
            'header': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
        }

class TaskFileForm(ModelForm):
    class Meta:
        model = TaskFile
        fields = ['file']
        widgets = {
        }


class InvitationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InvitationForm, self).__init__(*args, **kwargs)
        self.fields['to_user'].queryset = User.objects.exclude(username=user.username)

    class Meta:
        model = InviteProj
        fields = ['to_user']
        widgets = {
            'to_user': Select(attrs={
                'class': 'form-control py-1',
            }),
        }