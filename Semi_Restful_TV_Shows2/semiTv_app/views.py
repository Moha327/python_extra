from django.shortcuts import redirect, render
from . import models
from .models import *

import datetime
# Create your views here.
def index(request):
    return redirect("/shows")
def show_new(request):
    return render(request, 'index.html')

def process_data(request):
    if request.method=='POST':
        error=Show.objects.basic_validator(request.POST)
        if len(error)>0:
            
            return redirect("/shows/new")
        title=request.POST['title'] 
        network=request.POST['network']
        releaseDate=request.POST['date'] 
        desc=request.POST['desc']
        newShow=models.create_show(title, network, releaseDate, desc)
        request.session['id']=newShow.id
        return redirect('shows/'+str(request.session['id']))

def showInfo(request, id):
    show=models.Show_with_Id(id)
    context={
        'id':show.id,
        'title': show.title,
        'network': show.network,
        'releaseDate': show.releaseDate,
        'desc':show.desc,
        'lastupdated':show.updated_at,
    }
    return render(request, 'showInfo.html', context)      

def showAll(request):
    context={
        'All_shows':models.get_all_show(),
    }
    return render(request, 'all_shows.html', context)

def edit(request, id):
    show=models.Show_with_Id(id)
    date=show.releaseDate.strftime('%m/%d/%Y')
    context={
        'id':id,
        'title': show.title,
        'network': show.network,
        'releaseDate': date,
        'desc':show.desc,
    }
    return render(request, 'EditPage.html', context)   