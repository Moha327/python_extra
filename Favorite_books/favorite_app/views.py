from django.shortcuts import redirect, render
from .models import*
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.utils import timezone
def home(req):
    req.session['user'] = ""
    req.session['mymessages'] = ""
    return render(req,"home.html")
def createuser(req):
    errors = User.objects.basic_validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        email = req.POST['email']
        passwd = req.POST['passwd']
        confpw = req.POST['confirmpw']
        birthDate = req.POST['birth_date']
        try:
            if User.objects.get(email=email):
                errors["retitle"] = "this email is already exist"
        except:
            pass
        if passwd == confpw :
            User.objects.create(first_name=firstname,last_name=lastname,email=email,passwod=passwd)
            data ={
                "fname":firstname,
                "lastname":lastname,
                "email": email,
                "pass":passwd,
                "birth_date": birthDate
            }
            req.session['user'] = data
            return redirect('/welcome')
        return redirect("/")
def login(req):
    errors = User.objects.login_Validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        email = req.POST['loginemail']
        passwd = req.POST['loginpass']
        users = User.objects.filter(email=email)
        
        if len(users) == 0:
            return redirect("/")
        user = users.first()
        if user.passwod != passwd:
            return redirect("/")
        data ={
            'fname' : user.first_name,
            'password':user.passwod,
            'email' : user.email,
            'lastname' : user.last_name,
            'userid':user.id,
            
        }
        req.session['user'] = data
        return redirect('/welcome')

def welc(req):
    #all_comment = Comments.objects.all()
    books = Book.objects.all()
    if req.session['user'] :
        user = req.session['user']
        data={
        'user':user,
        'books':books,
        
        #'comments':all_comment
        }
        
        return render(req,"welcome.html",data)
    return redirect('/')
def logout(req):
    if req.session['user']:
        req.session.clear()
        return redirect('/')
def addBook(req , id):
    title = req.POST['titletext']
    users = User.objects.filter(id= id)
    user = users.first()
    desc = req.POST['desc']
    book = Book.objects.create(title = title , uploaded_by = user , desc = desc)
    context= {
        "Booktitle" :book.title,
        "Booktitle" :book.uploaded_by.first_name +" "+ book.uploaded_by.last_name,
        'bookids':book.id,
        'desc' : desc
        }
    return render(req,'welcome.html',context)
def deleteBook(req,id):
    books = Book.objects.filter(id=id)
    book_todelete = books.first()
    book_todelete.delete()
    return redirect('/welcome')
def showFave(req,id):
    user = req.session['user']
    book = Book.objects.get(id=id)
    bookid = book.id
    booktitle = book.title
    bookuploadedby = book.uploaded_by
    usersLiked = book.users_who_like.all()
    desc = book.desc
    context = {
        'Booktitle' : booktitle,
        'BookAuthor': bookuploadedby,
        'userswholike':usersLiked,
        'bookid':bookid,
        'desc':desc,
        'user':user,
        'uploaded_by': Book.objects.first().uploaded_by
    }
    return render(req,'favShow.html',context)
def addFavarit(req,id):
    users = req.session['user']
    user = User.objects.get(id = users['userid'])
    books = Book.objects.filter(id=id)
    book = books.first().id
    #user = users.first()
    #book_fave = Book.objects.update(users_who_like = users)
    user.liked_books.add(book)
    return redirect('/welcome')
def updatedes(req,id):
    desc= req.POST['updatetext']
    Book.objects.update(id=id , desc = desc)
    return redirect('/showbook/'+str(id))
def deletedes(req):
    req.session['description'] = ""
    return redirect('/showbook')
def unfavarit(req,id):
    users = req.session['user']
    user = User.objects.get(id = users['userid'])
    books = Book.objects.filter(id=id)
    book = books.first().id
    #user = users.first()
    #book_fave = Book.objects.update(users_who_like = users)
    user.liked_books.remove(book)
    return redirect('/welcome')