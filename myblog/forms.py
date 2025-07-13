from django import forms  # type: ignore
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title_tag", "title", "author", "category", "body"]

        widgets = {
            "title_tag": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title Tag"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "author": forms.Select(
                attrs={"class": "form-control dropdown-toggle", "placeholder": "Author"}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Content"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["category"].widget = forms.Select(
            choices=Category.objects.all().values_list("name", "name"),
            attrs={"class": "form-control dropdown-toggle", "placeholder": "Category"},
        )


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title_tag", "title", "body"]

        widgets = {
            "title_tag": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title Tag"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Content"}
            ),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Category Name"}
            ),
        }
