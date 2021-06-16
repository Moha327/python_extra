from django.shortcuts import HttpResponse, redirect,render 
from django.http import JsonResponse
from time import gmtime, strftime

def index(request):

    return render(request,'index.html')
    return redirect(base)

def index2(request):
    your_name = request.POST['Your Name']
    dojo_location = request.POST['Dojo Location']
    favorite_language = request.POST['Favorite Language']
    comment = request.POST['Comment']

    context = {
         "Name" : your_name,
         "Location" :dojo_location,
         "Language" : favorite_language,
         "Comm" : comment
    }
    return render(request,'index2.html',context)
    return redirect("/base2")
    