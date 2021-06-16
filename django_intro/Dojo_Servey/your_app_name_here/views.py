from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request,'index.html')

def check_credantial(username):
    if username == "khalil":
        return True
    return False


def show(request):
    if request.method == "POST":
        request.session['username']=request.POST['username']
        request.session['Location']=request.POST['Location']
        request.session['Language']=request.POST['Language']
        request.session['area']=request.POST['area']

    return redirect('/result')

def success(request):
    return render(request,'show.html')
