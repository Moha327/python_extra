from django.db.models.expressions import Ref
from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse
from . import models
import bcrypt
from django.contrib import messages
def index(request):
    return render(request , 'index.html')

def wall(request):
    if 'id' in request.session:
        context={
            'all_post':models.Post.objects.all().order_by('created_at').reverse(),
        }
        return render(request,'wall.html',context)
    else:
        return redirect('/')
def commenting(request,num):
    this_user=models.User.objects.get(id=request.session['id'])
    post=models.Post.objects.get(id=num)
    if request.method == 'POST':
        if 'comment_message' in request.POST :
            comment_message = request.POST['comment_message']
        else:
            comment_message=None
        models.Comment.objects.create(comment_message=comment_message,post=post,user=this_user)
        return redirect('/wall')

def posting(request):
    if request.method == 'POST':
        this_user=models.User.objects.get(id=request.session['id'])
        post_message=request.POST['post_message']
        this_user.posts.create(post_message=post_message,user=this_user)
        return redirect('/wall')

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(error) > 0:
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
                user=models.create_user(first_name,last_name,email,pw_hash)
                request.session['id']=user.id
                request.session['first_name']=user.first_name
                request.session['last_name']=user.last_name
                return redirect('/wall')

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
            return redirect('/wall')
        return redirect('/')