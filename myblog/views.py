from django.shortcuts import render, get_object_or_404
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
from django.http import HttpResponseRedirect


class LikesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["likes"] = self.object.number_of_likes()
        context["liked"] = self.request.user.is_authenticated and self.object.likes.filter(id=self.request.user.id).exists()
        return context


class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"
    ordering = ["-created_at"]


class ArticleDetailView(LikesMixin, DetailView):
    model = Post
    template_name = "myblog/article_detail.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = "myblog/update_post.html"
    # fields = ['title_tag', 'title', 'body']
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = "myblog/delete_post.html"
    success_url = reverse_lazy("home")


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "myblog/add_category.html"
    success_url = reverse_lazy("home")


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(
        request,
        "myblog/categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_posts},
    )


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse_lazy("article-detail", args=[str(pk)]))
