from django.contrib.auth import get_user
from django.views import View
from django.urls import reverse
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


