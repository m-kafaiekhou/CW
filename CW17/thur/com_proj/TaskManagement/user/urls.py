from django.urls import path
from .views import signup_view, ProfileView


urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]
