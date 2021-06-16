from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    clients = models.ManyToManyField(Book,related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    notes = models.IntegerField(null=True)

# def addOneBook(title,desc):
#     new_book = Book.objects.create(title=title,desc=desc)
#     return new_book

# def allBooks():
#     return Book.objects.all()
# def getBook():
#     return Book.objects
# book1=Book.objects.get(id=1)  
# book2=Book.objects.get(id=2)
# book3=Book.objects.get(id=3)  
# author2=Author.objects.get(id=2)
# author2.clients.add(book1)
