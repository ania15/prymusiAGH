from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from books.models import Book
# Create your views here.

def index(request):
    print(request.user)
    return render (request, "index.html")

def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "books_list.html", context)

def hello_world(request):
    our_context = { "time": datetime.now()}
    return render(request, template_name="index.html", context=our_context)
