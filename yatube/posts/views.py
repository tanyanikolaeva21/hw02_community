from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    title = 'Это главная страница проекта Yatube'
    posts = posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
