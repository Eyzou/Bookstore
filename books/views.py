from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author
from .forms import BookForm, AuthorForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
# def index(request):
#     return HttpResponse("Hello,world. You are at the books index.")

class IndexView(generic.ListView):
    template_name ="books/index.html"
    context_object_name="book_list"

    def get_queryset(self):
        return Book.objects.all()
    
@login_required
def addBook(request):
    if request.method =="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = BookForm()
    
    return render(request, 'books/add_book.html', {'form': form })

@login_required
def deleteBook(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('/')

@login_required
def editBook(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/edit_book.html', {'form' : form })

@login_required
def addAuthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    
    return render(request, 'books/add_author.html', {'form' : form })

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request,user)
            return HttpResponseRedirect(reverse('books:index'))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form })

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer