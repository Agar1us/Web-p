from django.forms import ModelForm, Select

from .models import *
from django import forms


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