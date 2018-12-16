from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from .views import BlogDetailView, BlogListView
from .admin import admin_site

urlpatterns = [
    path('', lambda request: render(request, 'mag/index.html'), name='home'),
    path('blogs', BlogListView.as_view(), name='blog_list'),
    path('blogs/<str:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('admin/', admin_site.urls),
]