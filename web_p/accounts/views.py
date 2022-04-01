from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from .forms import AvatarSettings, PasswordSettings, UserSettings
from .models import Avatar
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required


class ProfileSettingView(View):
    context = {
        'pagename': 'Настроки профиля',
    }

    @method_decorator(login_required)
    def get(self, request):
        self.context['name'] = request.user
        self.context['form'] = UserSettings(instance=request.user)
        self.context['avatar_form'] = AvatarSettings()
        self.context['change_password'] = PasswordSettings()
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            self.context['user_avatar'] = avatar[0].image
        return render(request, 'settings.html', self.context)

    @method_decorator(login_required)
    def post(self, request):
        if request.POST.get('avatar_form', None):
            avatar = Avatar.objects.filter(user=request.user)
            if not avatar:
                avatar = Avatar(user=request.user)
            else:
                avatar = avatar[0]
            form = AvatarSettings(request.POST, request.FILES, instance=avatar)
            if form.is_valid():
                form.save()
        elif request.POST.get('change_password', None):
            form = PasswordSettings(request.POST, instance=request.user)
            if form.is_valid():
                password = request.POST.get('password')
                new_password = request.POST.get('new_password', None)
                if new_password == password:
                    request.user.set_password(password)
                    request.user.save()
        else:
            form = UserSettings(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        return redirect(reverse('setting'))


def profile_page(request):
    context = {
        'pagename': 'Профиль',
    }
    return render(request, 'profile.html', context)

