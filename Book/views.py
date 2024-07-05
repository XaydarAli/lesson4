from django.shortcuts import render
from .models import Book
def homepage(request):
    return render(request,"homepage.html")
def author(request):
    return render(request,"author.html")
def books(request):
    books=Book.objects.all()
    return render(request,"books.html",{'books':books})
