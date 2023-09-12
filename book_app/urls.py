from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    path('<int:book_pk>', views.BookView.as_view()),
    path('<int:book_pk>/review/', include('review_app.urls'))
]