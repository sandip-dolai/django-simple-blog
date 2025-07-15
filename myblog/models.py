from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.urls import reverse  # type: ignore
from ckeditor.fields import RichTextField  # type: ignore


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home", args=[str(self.id)])


class Post(models.Model):
    title_tag = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    snippet = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title + " by " + self.author.username

    def get_absolute_url(self):
        return reverse("article-detail", args=[str(self.id)])

    def number_of_likes(self):
        return self.likes.count()
