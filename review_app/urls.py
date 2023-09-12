from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('<int:review_pk>', views.ReviewView.as_view())
]