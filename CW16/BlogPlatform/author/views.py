from django.shortcuts import render, get_object_or_404
from .models import Author

# Create your views here.


def author_view(request):
    author_list = Author.objects.all().order_by('name')
    return render(request, 'author/author_list.html', {'author_list': author_list})


def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author':author})