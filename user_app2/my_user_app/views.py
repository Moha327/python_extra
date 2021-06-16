from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    context = {
    	"user_app": User.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    request.session.add()
    return redirect("/")
