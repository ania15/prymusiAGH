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

def book_details(request, book_id):
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "book_details.html", context)

from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    
    if request.method == "POST":
        # stworz nowego uzytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #formularz poprawny, mozna zapisac uzytkownika
            form.save()
            #przekierowanie na stronę z podziękowaniem
            return render(request,"registration/signup_complete.html")
        
    else:
        #pokaz pusty formularz rejestracji
        form = UserCreationForm()
       
    context = {"form": form}
    return render(request, "registration/signup_form.html", context)


from django.contrib.auth.models import User
def profile_view(request):
    context = {"username": request.user}
    return render (request, 'profile_view.html', context)
