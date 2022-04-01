from django.contrib.auth import get_user
from django.views import View
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, DeleteView
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class ListInvitation(ListView):
    model = InviteProj
    template_name = 'main/invitation/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(to_user=self.request.user)


class CreateInvitation(CreateView):
    model = InviteProj
    form_class = InvitationForm
    template_name = 'main/invitation/create.html'
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.from_user = self.request.user
        self.object.proj = Proj.objects.filter(id=self.kwargs['id']).last()
        self.object.save()
        return redirect('home')


class DeleteInvitation(View):
    def get(self, request, id):
        invite = InviteProj.objects.filter(id=id).last()
        invite.delete()
        return redirect('list_invitation')


class AcceptInvitation(View):
    def get(self, request, id):
        invite = InviteProj.objects.filter(id=id).last()
        member = MembershipProject(proj=invite.proj, user=self.request.user)
        member.save()
        invite.delete()
        return redirect('list_invitation')
