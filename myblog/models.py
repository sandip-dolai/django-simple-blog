from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Post(models.Model):
    title_tag = models.CharField(max_length=100, default='My Blog')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' by ' + self.author.username
    
    
    
