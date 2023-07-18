from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse


# Create your views here.


def home(request):
    if request.GET.get('search', ''):
        search = request.GET.get('search')
        query = Post.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        ).distinct()

        context = {'query': query}
        return render(request, 'index.html', context=context)
    else:
        context = {}
        return render(request, 'index.html', context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    context = {}
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        authors = Author.objects.all()
        comments = Comment.objects.all()
        context = {"post": post, 'authors': authors, 'comments': comments}
        return render(request, "Blog/post.html", context)
    else:
        author = request.POST.get("author")
        comment = request.POST.get("comment")
        post = Post.objects.create(post= Post.objects.get(id=pk), author=author, content=comment)
        post.save()
        return redirect("Blog/post.html")


def category_list(request):
    all_category = Category.objects.all()
    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "Blog/category_details.html", {"category": category })
