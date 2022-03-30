from .models import *
from django import forms

class PostForm(forms.Form):

    header = forms.CharField(max_length=100, label='Заголовок', widget=forms.TextInput(attrs={'cols': 60, 'rows': 2}))
    content = forms.CharField(label='Содержание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 7}))


class CommentForm(forms.Form):

    content = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))

