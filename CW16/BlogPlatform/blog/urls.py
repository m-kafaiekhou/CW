from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('posts/', views.post_list_view, name='posts_list'),
    path('categories/', views.categories_list_view, name='categories_list'),
    path('posts/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('categories/<int:pk>/', views.category_detail_view, name='category_detail'),
]