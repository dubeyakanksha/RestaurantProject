from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import *
from.forms import contactform
from django.contrib.auth.decorators import login_required

def index(request):
    
    return render(request,"index.html")


def home(request):
    return render(request,"home.html")
               
def menu(request):
    starters=Starter.objects.all()
    salads=Salad.objects.all()
    specialtys=Specialty.objects.all()
    return render(request, "menu.html", {'starters':starters,'salads':salads,'specialtys':specialtys})
    

       


def booktable(request):
    if request.method=="POST":
        
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        persons=request.POST['persons']
        message=request.POST['message']
        print(name,email,phone,date,persons,message)
        ins = table(name=name,email=email,phone=phone,date=date,persons=persons,message= message)
        ins.save()
        print("data save in DB")
        return render(request,"booktable.html")	
    else:
        return render(request,"booktable.html")


def Event(request):
    if request.method=="POST":
        
        name=request.POST['name']
        phone=request.POST['phone']
        date=request.POST['date']
        event=request.POST['event']
        persons=request.POST['persons']
        
        print(name,phone,date,event,persons)
        var1 = program(name=name,phone=phone,date=date,event=event,persons=persons)
        var1.save()
        print("data save in DB")
        return render(request,"home.html")	
    else:
        return render(request,"Event.html")


def Contact1(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        var =response(name=name,email=email,phone=phone,subject=subject,message=message)
        var.save()
        return render(request,"contact.html")	
    else:
        return render(request,"contact.html")

def form(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
    form=contactform()
    return render(request,'form.html',{'form':form})



    
'''def index(request):
    salad1 = Salad()
    salad1.name='Curry1 Rice'
    salad1.desc='An So1uth Indian Recepie with Spieces Flavour'
    salad1.img='cake.jpg'
    salad1.price='$200'

    salad2 = Salad()
    salad2.name='Col1d coffee'
    salad2.desc='An s1mooth creamy'
    salad2.img='lobster-bisque.jpg'
    salad2.price='3100'

    salad3 = Salad()
    salad3.name='Chin1ese'
    salad3.desc='an i1talian recepie'
    salad3.img='lobster-roll.jpg'
    salad3.price='$5100'

    salads=[salad1,salad2,salad3]
    return render(request, "index.html", {'salads':salads})

def index(request):
    specialty1 = Specialty()
    specialty1.name='Curry Rice'
    specialty1.desc='An South Indian Recepie with Spieces Flavour'
    specialty1.img='cake.jpg'
    specialty1.price='200'

    specialty2 = Specialty()
    specialty2.name='Cold coffee'
    specialty2.desc='An smooth creamy'
    specialty2.img='lobster-bisque.jpg'
    specialty2.price='300'

    specialty3 = Specialty()
    specialty3.name='Chinese'
    specialty3.desc='an italian recepie'
    specialty3.img='lobster-roll.jpg'
    specialty3.price='500'

    specialtys=[specialty1,specialty2,specialty3]
    return render(request, "index.html", {'specialtys':specialtys})'''


