from django.contrib import admin


from books.models import Book # NEW
from books.models import Author
from books.models import Review


admin.site.register(Book)
admin.site.register(Author)

admin.site.register(Review) # NEW
