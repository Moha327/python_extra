from django.shortcuts import render, HttpResponse , redirect
from .models import *
# def index(request):
#     context = {
#         "dojos": Dojo.objects.all(),
#         'ninjas': Ninja.objects.all(),
#         }
#     return render(request,'index.html',context)
	
# def add_dojo(request):
#     Dojo.objects.create(name = request.POST['Name'], city=request.POST['City'], state=request.POST['State'])
#     return redirect('/')

# def add_ninja(request):
#     Ninja.objects.create(first_name = request.POST['First_Name'] , last_name = request.POST['Last_Name'], dojo = Dojo.objects.get(name = request.POST['Dojo_school']))
#     return redirect('/')

def index(request):
    hammouz={
        "moh":Dojo.objects.all(),
        "hamm":Ninja.objects.all()
    }
    return render(request,'index.html',hammouz)

def add_dojo(request):
    Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])

    return redirect('/')

def add_ninja(request):
    dojo=Dojo.objects.get(id=request.POST['sel'])
    Ninja.objects.create(first_name = request.POST['fname'],last_name= request.POST['lname'],dojo=dojo)

    return redirect('/')