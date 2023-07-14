from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Author, Comment

# Create your views here.


def home_page_view(request):
    return render(request, 'blog/home.html')


def post_list_view(request, category=None):
    if category:
        posts_list = Post.objects.filter(status='pub', category__id=category).order_by('-datetime_modified')
    else:
        posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def categories_list_view(request):
    categories_list = Category.objects.all().order_by('name')
    return render(request, 'blog/categories_list.html', {'categories_list': categories_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {'category': category})
