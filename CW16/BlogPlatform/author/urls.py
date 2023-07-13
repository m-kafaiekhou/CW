from django.urls import path
from .views import author_view, author_detail_view


urlpatterns = [
    path('', author_view, name='author_list'),
    path('<int:pk>/', author_detail_view, name='author_detail'),
]