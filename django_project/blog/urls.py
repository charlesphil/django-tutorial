from django.urls import path
from . import views

# Defines routes inside of blog route
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
