from django import forms
from django.contrib.auth.models import User
from .models import Avatar


class UserSettings(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomUsername',
                'placeholder': 'Имя пользователя',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustom01',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustom02',
                'placeholder': 'Фамилия',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomEmail',
                'placeholder': 'E-mail',
            }),
        }


class PasswordSettings(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomPassword',
                'placeholder': 'Новый пароль',
            }),
        }
        labels = {
            'password': 'Новый пароль'
        }

    new_password = forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'validationCustomNewPassword',
            'placeholder': 'Повторите пароль',
        }),
    )


class AvatarSettings(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'id': 'validationImage',
                'placeholder': 'Аватар',
            }),
        }
