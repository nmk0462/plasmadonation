from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import User
from .models import donar
from .models import requests1
from .models import mobs
from django.core import serializers
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request, "your/login.html",{"hy":tt})
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            tt=0
            gh=requests1.objects.all()
            for g in gh:
                tt=tt+1
            try:
                juju=mobs.objects.get(usrr=request.session['username'])
            except:
                juju=None
            if juju:
                login(request, user)
                return render(request,"your/form.html",{"hy":tt})
            else:
                return render(request,"your/verif.html",{"hy":tt})

          
           
        
        else:
            return render(request, "your/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "your/login.html")
def logout_view(request):
    if request.session.has_key('username'):

       del request.session['username']

  
    logout(request)
    
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        try:
            yu=User.objects.filter(email=email)
        except:
            yu=None
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if username=="" or email=="" or password=="" or confirmation=="":
            return render(request, "your/register.html", {
                "message": "Please fill all the details!!"
            }) 
        else:          
            if yu:
               return render(request, "your/register.html", {
                "message": "Email already in use :("
               })
            else:
               if password != confirmation:
                  return render(request, "your/register.html", {
                "message": "Passwords must match."
                   })

        # Attempt to create new user
               try:
                  user = User.objects.create_user(username, email, password)
                  user.save()
               except IntegrityError:
                  return render(request, "your/register.html", {
                "message": "Username already taken."
                  })
               request.session['username'] = username
               request.session['password'] = password
               tt=0
               gh=requests1.objects.all()
               for g in gh:
                  tt=tt+1
               return render(request,"your/verif.html")
        
        
    else:
        return render(request, "your/register.html")
def donate(request):
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request,"your/donar.html",{"hy":tt})
def sub(request):
    try:
        lp=donar.objects.get(name=request.session['username'])
    except:
        lp=None
    if lp:
        tt=0
        gh=requests1.objects.all()
        for g in gh:
           tt=tt+1
        ss = "You have already submitted your details!!!"
        return render(request,"your/form.html",{"hy":tt,"msg":ss})
    else:
        pp=donar()
        pp.name=request.session['username']
        rtt=mobs.objects.get(usrr=request.session['username'])
        pp.mobile=rtt.num
        pp.distr=request.POST.get("district")
        pp.group=request.POST.get("group")
        pp.diag=request.POST.get("dg")
        pp.save()
        tt=0
        gh=requests1.objects.all()
        for g in gh:
           tt=tt+1
        ss = "Sucessfully submitted,you will recieve a phone call if someone needs your help.Thank you!!!"
        return render(request,"your/form.html",{"hy":tt,"msg":ss})
def search(request):
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return  render(request,"your/srh.html",{"hy":tt})
def find(request):
    sd=None
    dd=request.POST.get("dis")
    try:
        sd=donar.objects.filter(distr=dd)
    except:
        sd=None
    if sd:
        tt=0
        gh=requests1.objects.all()
        for g in gh:
            tt=tt+1
        return render(request,"your/find.html",{"fg":sd,"hy":tt})
    else:
        tt=0
        gh=requests1.objects.all()
        for g in gh:
            tt=tt+1
        ji="UNFORTUNATELY, THERE ARE NO PLASMA DONORS IN YOUR AREA.TRY SEARCHING IN YOUR NEARBY DISTRICTS OR MAKE A REQUEST BELOW."
        return render(request,"your/req.html",{"fg":dd,"hy":tt,"gyu":ji})
def req(request):
    try:
        hu=requests1.objects.get(name=request.session['username'])
    except:
        hu=None
    if hu:
        tt=0
        gh=requests1.objects.all()
        for g in gh:
           tt=tt+1
        ss = "You have already submitted a request!!"
        return render(request,"your/form.html",{"hy":tt,"msg":ss})
    else:
        pl=requests1()
        pl.name=request.session['username']
        rt=mobs.objects.get(usrr=request.session['username'])
        pl.mobile=rt.num
        pl.distr=request.POST.get("district")
        pl.group=request.POST.get("group")
        pl.save()
        tt=0
        gh=requests1.objects.all()
        for g in gh:
           tt=tt+1
        ss = "Request submitted! Kindly wait until someone responds to your request.."
        return render(request,"your/form.html",{"hy":tt,"msg":ss})
def ffo(request):
        tt=0
        try:
            gh=requests1.objects.all()
        except:
            gh=None
        for g in gh:
            tt=tt+1
        ji="MAKE A REQUEST!"
        return render(request,"your/req.html",{"hy":tt,"gyu":ji})
def hlp(request):
    gh=requests1.objects.all()
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request,"your/help.html",{"gg":gh,"hy":tt})
def dels(request):
    try:
        rr=donar.objects.filter(name=request.session['username'])
    except:
        rr=None
    try:
        hh=requests1.objects.filter(name=request.session['username'])
    except:
        hh=None
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request,"your/dels.html",{"q":rr,"w":hh,"hy":tt})
def del1(request,mn):
    fg=donar.objects.filter(name=mn)
    fg.delete()
    try:
        rr=donar.objects.filter(name=request.session['username'])
    except:
        rr=None
    try:
        hh=requests1.objects.filter(name=request.session['username'])
    except:
        hh=None
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request,"your/dels.html",{"q":rr,"w":hh,"hy":tt})
def del2(request,mn1):
    fg=requests1.objects.filter(name=mn1)
    fg.delete()
    try:
        rr=donar.objects.filter(name=request.session['username'])
    except:
        rr=None
    try:
        hh=requests1.objects.filter(name=request.session['username'])
    except:
        hh=None
    tt=0
    gh=requests1.objects.all()
    for g in gh:
        tt=tt+1
    return render(request,"your/dels.html",{"q":rr,"w":hh,"hy":tt})
def next(request):
    tt=0
    gh=requests1.objects.all()
    kok=request.POST.get('aa')
    try:
        jk=mobs.objects.get(num=kok)
    except:
        jk=None
    for g in gh:
        tt=tt+1
    try:
        ty=mobs.objects.get(usrr=request.session['username'])
    except:
        ty=None
    if ty:
        user = authenticate(request, username=request.session['username'], password=request.session['password'])
        login(request, user)
        return render(request,"your/form.html",{"hy":tt})
    else:
        if kok!=None:
           if jk:
               opp="Number already in use :("
               return render(request,"your/verif.html",{"mess":opp})    
           else:          
               hu=mobs()
               hu.num=request.POST.get('aa')
               hu.usrr=request.session['username']
               hu.save()
               user = authenticate(request, username=request.session['username'], password=request.session['password'])
               login(request, user)
               return render(request,"your/form.html",{"hy":tt})
        else:
           opp="Please enter a valid phone number!!"
           return render(request,"your/verif.html",{"mess":opp})
def info(request):
    tt=0
    try:
        gh=requests1.objects.all()
    except:
        gh=None
    for g in gh:
        tt=tt+1
    return render(request,"your/info.html",{"hy":tt})
@csrf_exempt
def chk(request,ppn):
    try:
        phn=mobs.objects.get(num=ppn)
    except:
        phn=None
    if request.method=="GET":
        if phn:
           return JsonResponse("yes",safe=False)
        else:
           return JsonResponse("no",safe=False)
    else:
        return JsonResponse({"error":"Try GET"},status=404)
    

    

        


