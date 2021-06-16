import random
from django.shortcuts import redirect, render, HttpResponse
def ss():
    return redirect('/')
def index(request):
    if request.method == "POST": 
        request.session['radm']=random.randint(1, 100)
        print(request.session['radm'])
        request.session['numb']=int(request.POST['num'])
        if request.session['numb']>request.session['radm']:
            request.session['x']='Too high!'
        elif request.session['numb']<request.session['radm']:
            request.session['x']='Too low!'
        else:
            request.session['x']='right'
    return render(request,'index.html')

def s(request):
    request.session.clear()
    return redirect("/")

