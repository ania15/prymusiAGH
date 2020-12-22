from django.contrib import admin


from books.models import Book # NEW

admin.site.register(Book) # NEW
