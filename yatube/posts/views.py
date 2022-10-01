from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_PER_PAGE = 10


def index(request):
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
