from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

class BlogListView(ListView):
    model=Blog
    context_object_name='blogs'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name='blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Blog.objects.all()[:5]
        context["latest_similar"] = Blog.objects.filter(tags__in=self.get_object().tags.all())
        return context
    