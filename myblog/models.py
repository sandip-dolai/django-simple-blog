from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.urls import reverse # type: ignore

class Post(models.Model):
    title_tag = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' by ' + self.author.username
    
    def get_absolute_url(self):
        return reverse('article-detail', args = [str(self.id)])
    
    
    
