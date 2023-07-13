from django.urls import path, include
from .views import home_page_view, post_list_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('posts/', post_list_view, name='posts_list'),
]