from django.urls import path, include
from . import views
from .views import AuthorViewSet , BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

app_name = "books"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/addbook", views.addBook, name="addBook"),
    path("/deletebook/<int:pk>", views.deleteBook, name= "deleteBook"),
    path("/editbook/<int:pk>", views.editBook, name="editBook"),
    path("/addauthor", views.addAuthor, name="addAuthor"),
    path("/register", views.register, name="register"),
    path("", include(router.urls))
]
