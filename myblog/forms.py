from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_tag', 'title', 'author', 'body']
        
        widgets = {
            'title_tag' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Tag'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'author': forms.Select(attrs={'class':'form-control dropdown-toggle', 'placeholder':'Author'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_tag', 'title', 'body']
        
        widgets = {
            'title_tag' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Tag'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
        }