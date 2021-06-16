from django.shortcuts import render, HttpResponse

    # return HttpResponse("this is the equivalent of @app.route('/')!")

def index(request):
     
    return HttpResponse("placeholder to display a new form to create a new blog")


def root_method(request):
    return HttpResponse("String response from root_method")

def another_method(request):
    return redirect("/blog")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def another_method(request):
    return redirect("/blog/create")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number {number}")

def root(request):
    return HttpResponse("String response from root_method")

def destroy(request,number):

    return redirect("/blogs")

def redirected_method(request):
    data={
        "title": "blogs",
        "content": "content-hhhhhh"
    }
    return JsonResponse(data)