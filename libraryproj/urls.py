"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import books_list
from books.views import index
from books.views import hello_world
from books.views import book_details
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from books.views import user_signup, BookList, AuthorList, AuthorDetail
from books.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', user_signup, name='user_signup'),
    path('accounts/profile/', profile_view, name='user_profile'),
    path('books/', BookList.as_view(), name="book_list"),
    path('', index, name="index"),
    path('hello/', hello_world),
    path('authors/', AuthorList.as_view(), name="author_list"),
    path('authors/<int:author_id>', AuthorDetail.as_view(), name="author_details"),
    path('books/<int:book_id>', book_details, name="book_details"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
