from .models import Category, Post, User


def cats_menu(request):
    return {"cats_menu": Category.objects.all()}
