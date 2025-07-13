from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'myblog/home.html')


class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"
    ordering = ["-created_at"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "myblog/article_detail.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "myblog/add_category.html"
    success_url = reverse_lazy("home")


class UpdatePostView(UpdateView):
    model = Post
    template_name = "myblog/update_post.html"
    # fields = ['title_tag', 'title', 'body']
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = "myblog/delete_post.html"
    success_url = reverse_lazy("home")
