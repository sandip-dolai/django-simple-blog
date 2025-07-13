from django.urls import path # type: ignore
from .views import UserRegisterView
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]