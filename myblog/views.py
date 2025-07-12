from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'myblog/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'myblog/article_detail.html'