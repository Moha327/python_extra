from django.shortcuts import render,redirect
from .models import *
import re
from django.contrib import messages
import bcrypt



def root(request):
    return render(request , 'index.html')
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']

def add(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors = {}
    if len(request.POST["fname"]) < 2 :
        errors ["first_name"] = "This < 2"
       
    if len(request.POST["lname"]) < 2 :
        errors ["last_name"] = "This < 2"
        # for key, value in errors.items():
        #    if len(errors) > 0:
        #        messages.error(request,value)
        #        return redirect ('/')
    if not EMAIL_REGEX.match(request.POST['email']):               
            errors['email'] = "Invalid email address!"
            # for key, value in errors.items():
            #     if len(errors) > 0:
            #         messages.error(request,value)
            #         return redirect ('/')
    if len(request.POST["passwd"]) < 8:
        errors['passwd'] = "short"
    

        # for key, value in errors.items():
        #    if len(errors) > 0:
        #        messages.error(request,value)
        #        return redirect ('/')
    if request.POST["passwd"] != request.POST['conpasswd']:
        error['conpasswd'] = "no"
        for key, value in errors.items():
            if len(errors) > 0:
               messages.error(request,value)
               return redirect ('/')
    else:
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['passwd']
        conf=request.POST['conpasswd']

        if password==conf:
            hash = bcrypt.hashpw("request.POST['passwd']".encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name = first_name, last_name = last_name,email = email, passwd = hash)
            if 'name' not in request.session:
                request.session['name']= first_name
            return redirect('/success')
            
        return redirect('/')
def success(request):
    return render(request,"success.html")

# def logout(request):
#     del request.session['name']
#     return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user: #if len(user) > 0 :
        if bcrypt.checkpw(request.POST['passwd'].encode(), user[0].passwd.encode()):
            if 'name' not in request.session:
                request.session['name']=user[0].first_name
                return redirect('/success')
        return redirect('/')
    return redirect('/')