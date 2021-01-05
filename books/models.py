from django.db import models

# Create your models here.
class Book(models.Model):  
    title = models.CharField(max_length=100)    
    short_description = models.TextField()    
    published_at = models.DateTimeField()
    # dodane
    created_at = models.DateTimeField(null=True)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Książka: " + self.title

# b = Book()
# print(b)