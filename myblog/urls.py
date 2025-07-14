from django.urls import path  # type: ignore

# from . import views
from .views import (
    ArticleDetailView,
    HomeView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
    LikeView,
)

urlpatterns = [
    # path('', views.home, name='home'),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete-post"),
    path("add-category/", AddCategoryView.as_view(), name="add-category"),
    path("category/<str:cats>/", CategoryView, name="category"),
    path("like/<int:pk>", LikeView, name="like-post"),
]
