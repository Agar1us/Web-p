from django.contrib.auth import get_user
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class ProjView(View):
    def get(self, request):
        my_proj = Project.objects.filter(creator=request.user)
        return render(request, 'main/my_projects.html', {'my_proj': my_proj})


class CreateProj(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/create_project.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object = form.save()
        return redirect('my_projects')



class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'main/create_task.html'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.proj = Project.objects.get(id=self.kwargs['id'])
        self.object = form.save()
        return redirect('my_project', self.kwargs['id'])


class DetailProject(View):
    def get(self, request, id):
        proj = get_object_or_404(Project, id=id)
        tasks = Task.objects.filter(proj_id=id)
        return render(request, 'main/detail_project.html', {'proj': proj, 'tasks': tasks})


class DetailTask(CreateView):
    model = TaskFile
    form_class = TaskFileForm
    template_name = 'main/detail_task.html'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task = Task.objects.get(id=self.kwargs['id'])
        self.object = form.save()
        return redirect('task', self.kwargs['id'])

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        taskfiles = TaskFile.objects.filter(task_id=id)
        members = task.members.all()
        form = TaskFileForm()
        content = {
            'task': task,
            'taskfiles': taskfiles,
            'members': members,
            'form': form,
        }
        return render(request, 'main/detail_task.html', content)


class UpdateProj(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/update_project.html'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('my_project', self.kwargs['id'])


class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'main/update_task.html'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('task', self.kwargs['id'])


class DeleteProj(DeleteView):
    template_name = 'main/delete_project.html'
    model = Project
    model_form = ProjectForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('my_projects')

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('my_projects')


class DeleteTask(DeleteView):
    template_name = 'main/delete_task.html'
    model = Task
    model_form = TaskForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('my_projects')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('my_projects')


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
