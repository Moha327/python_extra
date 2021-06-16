from typing import ContextManager
from django.db.models.expressions import Ref
from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse
from . import models
import bcrypt
from django.contrib import messages

def index(request):
    if 'id' in request.session:
        return redirect('/books')

    return render(request,"index.html")

def books(request):
    context={
        'all_users':models.User.objects.all(),
        'user': models.User.objects.get(id=request.session['id'])
    }
    return render(request,'index2.html',context)
    

def register(request):

    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) == 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == "POST":
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            passwd=request.POST["passwd"]
            pw_hash = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()  # create the hash    
            conpasswd=request.POST["conpasswd"]
            if passwd==conpasswd:
                user=models.create_user(first_name,last_name,email)
                request.session['id']=user.id
                request.session['first_name']=user.first_name
                request.session['last_name']=user.last_name
                return redirect('/register')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        passwd=request.POST["passwd"]
        user = models.get_user(email)
        if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
        return redirect('/')
    
def welcome(request):
    return render(request, 'index2.html')