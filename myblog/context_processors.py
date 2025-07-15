from .models import Category


def cats_menu(request):
    return {"cats_menu": Category.objects.all()}
