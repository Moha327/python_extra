from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0


    return render(request, 'index.html')

def process_money(request):
    if request.POST['Farm'] == 'Farm':
        request.session['gold'] += random.randint(10, 20)
    elif request.POST['Farm'] == 'Cave':
        request.session['gold'] += random.randint(5, 10)
    elif request.POST['Farm'] == 'House':
        request.session['gold'] += random.randint(2, 5)
    elif request.POST['Farm'] == 'Casino':
        request.session['gold'] += random.randint(-50, 50)
    return redirect('/')


        
    if 'area' in request.session:
            if request.POST['which_form'] != 'register4':
                request.session['area'] =request.session['area'] + "\n" +"earned"+" " + str(request.session['gold'])+ " from the" +" " + str(request.session['name']) + " ! " +str(request.session['time'])
            elif request.POST['which_form'] == 'register4':
                request.session['area'] = request.session['area'] + "\n" + "earned a casino and lost "+ " " + str(request.session['gold']) + " ..Ouch.. "+ str(request.session['time'])
    else:
            if request.POST['which_form'] != 'register4':
                request.session['area'] ="earned"+" " + str(request.session['gold'])+ " from the" +" " + str(request.session['name']) + " ! " +str(request.session['time'])
            elif request.POST['which_form'] == 'register4':
                request.session['area'] ="\n" + "earned a casino and lost "+ " " + str(request.session['gold']) + " ..Ouch.. "+ str(request.session['time'])
    return redirect('/')