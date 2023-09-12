from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AuthorView.as_view()),
    path('<int:author_pk>', views.AuthorView.as_view())
]