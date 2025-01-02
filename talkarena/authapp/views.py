from django.shortcuts import render,redirect
from.models import *
from userapp.models import *
# Create your views here.

def ati(request):
    a=request.session.get('a_id')
    auth=atregdb.objects.all().count()
    bk=atapn.objects.filter(status=0).count()
    aprbk=atapn.objects.filter(status=1).count()
    dclnbk=atapn.objects.filter(status=2).count()
    at=atregdb.objects.filter(id=a)
    ar=atapn.objects.all()
    cont={
        'x':at,'a':ar,'auth':auth,'bk':bk,'aprbk':aprbk,'dclnbk':dclnbk
    }
    return render(request,'authindx.html',cont)

def atreg(request):
    return render(request,'authreg.html')

def atlog(request):
    return render(request,'authlog.html')

def atregdata(request):
    if request.method=='POST':
        atname=request.POST['atn']
        atmail=request.POST['atm']
        atprf=request.FILES['ati']
        atpsw=request.POST['atp']
        data=atregdb(atname=atname,atmail=atmail,atprf=atprf,atpsw=atpsw)
        data.save()
    return redirect('atlog')

def atlogdata(request):
    if request.method == "POST":
        atname=request.POST.get('atn')
        atpsw=request.POST.get('atp')
        if atregdb.objects.filter(atname=atname,atpsw=atpsw).exists():
           data = atregdb.objects.filter(atname=atname,atpsw=atpsw).values('id','atmail').first()
           request.session['a_id'] = data['id']
           request.session['email_a'] = data['atmail']
           request.session['username_a'] = atname
           request.session['password_a'] = atpsw
           return redirect('ati') 
        else:
            return render(request,'authlog.html',{'msg':'invalid user credentials'})
    else:
        return redirect('atlog')

def atlogout(request):
    del request.session['a_id']
    del request.session['email_a']
    del request.session['username_a']
    del request.session['password_a']
    return redirect('ati')

def ataprs(request):
    a=request.session.get('a_id')
    ata=atregdb.objects.filter(status=1,id=a)
    cont={
        'a':ata
    }
    return render(request,'ataprs.html',cont)

def atdecs(request):
    a=request.session.get('a_id')
    atd=atregdb.objects.filter(status=2,id=a)
    cont={
        'a':atd
    }
    return render(request,'atdecs.html',cont)

#apnts reqs

def atapnreq(request):
    a=request.session.get('a_id')
    con=atapn.objects.filter(status=0,aid=a)
    cont={
        'inf':con
    }
    return render(request,'atapnreqs.html',cont)

def atapna(request):
    a=request.session.get('a_id')
    con=atapn.objects.filter(status=1,aid=a)
    cont={
        'inf':con
    }
    return render(request,'atapnapr.html',cont)

def atapnapr(request,id):
    con=atapn.objects.filter(id=id).update(status=1)
    return redirect('atapna')

def atapnd(request):
    a=request.session.get('a_id')
    con=atapn.objects.filter(status=2,aid=a)
    cont={
        'inf':con
    }
    return render(request,'atapndec.html',cont)

def atapndec(request,id):
    con=atapn.objects.filter(id=id).update(status=2)
    return redirect('atapnd')

