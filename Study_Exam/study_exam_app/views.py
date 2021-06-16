from django.db.models.expressions import Ref
from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse
from . import models
import bcrypt
from django.contrib import messages
from .models import User, Car
from typing import ContextManager
def index(request):
    
    return render(request,"index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == "POST":
            name=request.POST["name"]
            email=request.POST["email"]
            passwd=request.POST["passwd"]
            alios=request.POST["alios"]
            release_date=request.POST["release_date"]
            pw_hash = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()  # create the hash    
            conpasswd=request.POST["conpasswd"]
            if passwd==conpasswd:
                user=models.create_user(name,alios,email,pw_hash,release_date)
                request.session['id']=user.id
                request.session['name']=user.name
                request.session['release_date']=user.release_date
                request.session['email']=user.email
                return redirect('/welcome')
def welcome(request):
    if 'id' in request.session:
        context={
             'all_users':models.User.objects.all(),
            'users':models.get_user(request.session['id']),
            
        }
        return render(request,'welcome.html', context)
    else:
        return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')
def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        passwd=request.POST["passwd"]
        user = models.get_user(email) 
        if user: 
            logged_user = user
       
            if bcrypt.checkpw(passwd.encode(), logged_user.passwd.encode()):
            
                request.session['id']=user.id
                request.session['name']=user.name
                request.session['alios']=user.alios
                request.session['email']=user.email
                return redirect('/welcome')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect("/")
def delete(request,id):
    x=User.objects.get(id = id)
    x.delete()
    return redirect('/welcome')
def profile(request,id):
    context={
             'all_users':models.User.objects.all(),
            'users':models.get_this_user(id),
        }
    print(context['users'].name)
    print(context['users'].email)
    print(context['users'].alios)
    return render(request,"welcome2.html",context)       