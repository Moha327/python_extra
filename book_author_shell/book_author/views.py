from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
        # 'books':models.allBook()
        }
    return render(request, 'index.html' , context)

def register(request):
    if request.method=="POST":
        Book.objects.create(title=request.POST['title'],desc=request.POST['description'])
        

    
    return redirect('/')



def index2(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        }
    return render(request, 'book.html' , context)

def display(request,id1):
    book = Book.objects.get(id =id1)
    context={
        "books":book,
        "authors":Author.objects.all()
    }
    
    return render(request, 'book.html' , context)


def add(request,id1):
     if request.method=="POST":
        author=Author.objects.get(id=request.POST['selects'])
        book=Book.objects.get(id=id1)
        book.authors.add(author)
     return redirect(f"/books/{id1}")

def index3(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        }
    return render(request, 'author.html' , context)

def add2(request,id1):
    author = Author.objects.get(id =id1)
    context={
        "authors":author,
        "book":Book.objects.all()
    }
    
    return render(request, 'author2.html' , context)

def register2(request):
    if request.method=="POST":
        Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['notes'])
        

    
    return redirect('/author')

def index4(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        }
    return render(request, 'author2.html' , context)

    
def add3(request,id1):
     if request.method=="POST":
        author=Author.objects.get(id=request.POST['select'])
        book=Book.objects.get(id=id1)
        author.clients.add(author)
     return redirect(f"/author/{id1}")

# def addBook(request):
 #  if request.method == 'POST':
 #     title = req
 #     desc = req
 # def showBook(request,id):
 # context = {
 # 'this_book':models.getBook(id)
 # }
 #   return render(request,book.html)