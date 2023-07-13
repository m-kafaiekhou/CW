from django.shortcuts import render
from .models import Post

# Create your views here.


def home_page_view(request):
    return render(request, 'blog/home.html')


def post_list_view(request):
    posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})