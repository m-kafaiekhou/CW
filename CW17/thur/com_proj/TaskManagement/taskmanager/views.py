from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Task, Note, Category

# Create your views here.


def home_page_view(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'taskmanager/home.html', context=context)


def search_view(request):
    if request.GET.get('search', ''):
        search = request.GET.get('search')
        if search.startswith("#"):
            query = Task.objects.filter(tags__name__icontains=search[1:])
        else:
            query = Task.objects.filter(
                Q(title__icontains=search) | Q(tags__name__icontains=search)
            ).distinct()
        paginator = Paginator(query, 6)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj, 'search': search}
        return render(request, 'taskmanager/search.html', context=context)
    else:
        return render(request, 'taskmanager/search.html')


def tasks_list_view(request):
    tasks = Task.objects.all()
    order = request.GET.get('order', 'due_date')
    ad = request.GET.get('ad', 'asc')
    if ad == "desc":
        tasks = tasks.order_by(f"-{order}")
    else:
        tasks = tasks.order_by(order)

    paginator = Paginator(tasks, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'order': order, 'ad': ad}

    return render(request, 'taskmanager/view_all.html', context=context)


def task_detail_view(request, pk):
    task = Task.objects.get(id=pk)
    notes = Note.objects.filter(task=task)
    context = {'task': task, 'notes': notes}
    return render(request, 'taskmanager/task_detail.html', context=context)


def categories_view(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'taskmanager/categories.html', context=context)


def category_task_view(request, cat):
    tasks = Task.objects.filter(category__id=cat)
    paginator = Paginator(tasks, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'taskmanager/home.html', context=context)


def category_create_view(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    Category.objects.create(name=title, description=description)
    return redirect('categories')
