from django.shortcuts import render,HttpResponse,redirect

def index(request):
    if 't1' not in request.session:
        request.session['t1'] = 1
    else:
        request.session['t1']+= 1

    return render(request,'index.html')

def destroy(request):
    request.session.clear()
    return redirect('/')