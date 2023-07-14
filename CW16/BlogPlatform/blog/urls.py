from django.urls import path, include
from .views import (
    home_page_view, 
    post_list_view, 
    categories_list_view, 
    post_detail_view, 
    category_detail_view
)


urlpatterns = [
    path('', home_page_view, name='home'),
    path('posts/', post_list_view, name='posts_list'),
    path('categories/', categories_list_view, name='categories_list'),
    path('posts/<int:pk>/', post_detail_view, name='post_detail'),
    path('categories/<int:pk>/', category_detail_view, name='category_detail'),
    path('posts/category/<int:category>/', post_list_view, name='post_list_category'),
]