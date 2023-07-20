from django.urls import path
from .views import (
    home_page_view,
    search_view,
    tasks_list_view,
    task_detail_view,
    categories_view,
    category_task_view,
    category_create_view,
    task_create_view,
    task_cat_create_view,
)

urlpatterns = [
    path('', home_page_view, name="home"),
    path('search/', search_view, name="search"),
    path('tasks/', tasks_list_view, name="task_list"),
    path('task/<int:pk>/', task_detail_view, name="task_detail"),
    path('categories/', categories_view, name="categories"),
    path('categories/<str:cat>/', category_task_view, name="category_task"),
    path('category/create/', category_create_view, name='category_create'),
    path('task/create/', task_create_view, name='task_create'),
    path('task/create/<str:cat>/', task_cat_create_view, name="task_cat")
]
