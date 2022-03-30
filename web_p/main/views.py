from django.contrib.auth import get_user
from django.views import View
from django.urls import reverse
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class HomeView(View):

    def post(self, request):
        post = request.POST.get('post')
        author = request.POST.get('user')
        if post:
            return redirect(reverse('post', kwargs={'id': post}))
        if author:
            return
            return redirect(reverse('post', kwargs={'id': post}))

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'main/home.html', {'posts': posts})


class PostView(View):

    def get(self, request, id):
        posts = Post.objects.all()
        post = get_object_or_404(posts, id=id)
        comments = Comment.objects.filter(post_id=id)
        add_comment = CommentForm()
        return render(request, 'main/post.html', {'post': post, 'comments': comments, 'form': add_comment})

    @method_decorator(login_required)
    def post(self, request, id):
        post = Post.objects.get(id=id)
        print(id)
        print(post.content)
        form = CommentForm(request.POST)
        print('Коментарий')
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Comment.objects.create(**form.cleaned_data, author=get_user(request), post=post)
                print('ok')
                return redirect(reverse('post', kwargs={'id': id}))
            except:
                print('no')
                form.add_error(None, 'Ошибка, комментарий не написан')


class CreatePostView(View):

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                Post.objects.create(**form.cleaned_data, author=get_user(request))
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка, пост не опубликован')

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        return render(request, 'main/create_post.html', {'form': form })

class DeletePostView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect('home')