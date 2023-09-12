from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreView.as_view()),
    path('<int:genre_pk>', views.GenreView.as_view())
]