from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import udata,movie,theatre,confirm
from django.core.mail import send_mail
from random import randint
lp=''
rp=''

# Home pahe
def page(request):
    return render(request,'page.html')
#register page
def reg(request):
    global rp
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email'].lower()
        mobile=request.POST['mobile']
        password=request.POST['pwd']
        rp=udata(name=name,email=email,mobile=mobile,password=password)
        rp.save()    
        return render(request,'log.html')
    return render(request,'reg.html')   
#login page
def log(request):
    if request.method=="POST":
        email=request.POST['email'].lower()
        password=request.POST['pwd']
        global lp
        lp=udata.objects.filter(email=email,password=password)
        mn=movie.objects.all()
        tn=theatre.objects.all()
        if not lp:
            return render(request,'log.html',{'msg':"Check login details"})
        else:
            return render(request,'book.html',{'mn':mn,'tn':tn,'email':email})
            
    return render(request,'log.html')
#all movies list
def movies(request):
    ms=movie.objects.all()
    return render(request,'movies.html',{'ms':ms})
#detail data    
def detl(request,id):
    ms=movie.objects.get(id=id)
    return render(request,'detl.html',{'ms':ms})
#all theatre list
def theatres(request):
    ts=theatre.objects.all()
    return render(request,'theatres.html',{'ts':ts})
#serach for movie
def search(request):
    if request.method=='POST':
        name=request.POST['nm']
        sp=movie.objects.filter(movie_name__icontains=name)
        if sp:
            return render(request,'name.html',{'sp':sp})
        else:
            return HttpResponse("No movie")
      
#Tickcke booking page            
def book(request):
    if request.method=='POST':
        n='TK' 
        for i in range(0,4):
            n=n+str(randint(0,9))
        ticket_id=n   
        mname=request.POST['mname']
        tname=request.POST['tname']
        date=request.POST['date']
        time=request.POST['time']
        sat=request.POST['seat']
        da=confirm(ticket_id=ticket_id,movie_name=mname,theatre_name=tname,date=date,time=time,seat=sat)
        da.save()
        ms=movie.objects.filter(movie_name=mname)
        ts=theatre.objects.filter(theatre_name=tname)
        if ms and ts:
            tid=request.session['id']=da.ticket_id
            to=lp.email
            name=lp.name
            sub="Movie ticket confirmation"
            sender='sandeep96424@yahoo.in'
            msg="Hello Mr/Ms:"+name+"\n"+"Ticket_ID:"+tid+"\n"+"Movie Name:"+request.POST['mname']+"\n"+"Theatre Name:"+request.POST['tname']+"\n"+"Date:"+request.POST['date']+"\n"+"Show Time:"+request.POST['time']+"\n"+"Seats:"+request.POST['seat']+"\n"+"-Thank you for Using Ticket Booking"+"\n"+"it is auto generated mail"
            send_mail(sub,msg,sender,[to])
            return render(request,'final.html',{'movie_name':da.movie_name,'theatre_name':da.theatre_name,'date':da.date,'time':da.time,'seat':da.seat,})
        else:
            return HttpResponse("Check details")          
    return render(request,'book.html')
#for retrieve ticket from db
def retrive(request):
    if request.method=="POST":
        tid=request.POST['tid']
        tk=confirm.objects.filter(ticket_id=tid)
        if tk:
            return render(request,'ticket.html',{'tk':tk})
        else:
            return render(request,'ticket.html',{'msg':"Enter Valid Ticket_ID"})    
    return render(request,'ticket.html')        
    
def forgot(request):
        if request.method=="POST":
            email=request.POST['ema']
            ft=udata.objects.get(email=email)
            if ft:
                to=email
                pwd=ft.password
                name=ft.name
                sub="password reset"
                msg="Hello Mr/Ms:"+name+"\n"+"your password:"+"\n"+pwd
                sender="sandeep96424@yahoo.in"
                send_mail(sub,msg,sender,[to])
                return render(request,'forgot.html',{'msg':'password sent sucessfully to your email'})        
            else:
                return HttpResponse("Enter correct Email id")   
        return render (request,'forgot.html')

#for movie full details & trailer
def m1(request):
    return render(request,'movies/m1.html')
def m2(request):
    return render(request,'movies/m2.html')
def m3(request):
    return render(request,'movies/m3.html') 




