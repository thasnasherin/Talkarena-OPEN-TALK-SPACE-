from django.shortcuts import render,redirect
from adminapp.models import *
from userapp.models import *
from psyapp.models import * 
from authapp.models import * 
# Create your views here.

def ai(request):
    psyapr=pregdb.objects.filter(status=1).count()
    authapr=atregdb.objects.filter(status=1).count()
    rusr=regdb.objects.all().count()
    cont=contdb.objects.all().count()
    abks=atapn.objects.all().count()
    pbks=psyapn.objects.all().count()
    cnt={
        'psy':psyapr,'auth':authapr,'usr':rusr,'cont':cont,'ab':abks,'pb':pbks
    }
    return render(request,'aindx.html',cnt)

def frm(request):
    return render(request,'frm.html')

def tab(request):
    return render(request,'tab.html')

def rinfo(request):
    con=regdb.objects.all()
    cont={
        'inf':con
    }
    return render(request,'reginfo.html',cont)
    
def contp(request):
    con=contdb.objects.all()
    cont={
        'inf':con
    }
    return render(request,'contp.html',cont)

def pinfo(request):
    con=pregdb.objects.all()
    cont={
        'inf':con
    }
    return render(request,'pregs.html',cont)

def atinfo(request):
    con=atregdb.objects.all()
    cont={
        'inf':con
    }
    return render(request,'atregs.html',cont)

def bladd(request):
    return render(request,'bladd.html')

def bldata(request):
    if request.method=='POST':
        bwrd=request.POST['bl']
        data=bldb(bwrd=bwrd)
        data.save()
    return redirect('bltab')

def bltab(request):
    info=bldb.objects.all()
    cont={
        'inf':info
    }
    return render(request,'bltab.html',cont)

def blu(request,bd):
    info=bldb.objects.filter(id=bd)
    cont={
        'inf':info
    }
    return render(request,'blupd.html',cont)

def blup(request,bd):
    if request.method=='POST':
        bwrd=request.POST['bl']
        bldb.objects.filter(id=bd).update(bwrd=bwrd)
    return redirect('bltab')

def bldl(request,bd):
    bldb.objects.filter(id=bd).delete()
    return redirect('bltab')

#aprs and decs pages of psys & auths
def preq(request):
    con=pregdb.objects.filter(status=0)
    cont={
        'inf':con
    }
    return render(request,'psyreqs.html',cont)

def pa(request):
    con=pregdb.objects.filter(status=1)
    cont={
        'inf':con
    }
    return render(request,'paprd.html',cont)

def papr(request,id):
    con=pregdb.objects.filter(id=id).update(status=1)
    return redirect('pa')

def pd(request):
    con=pregdb.objects.filter(status=2)
    cont={
        'inf':con
    }
    return render(request,'pdec.html',cont)

def pdec(request,id):
    con=pregdb.objects.filter(id=id).update(status=2)
    return redirect('pd')

def atreq(request):
    con=atregdb.objects.filter(status=0)
    cont={
        'inf':con
    }
    return render(request,'atreqs.html',cont)

def ata(request):
    con=atregdb.objects.filter(status=1)
    cont={
        'inf':con
    }
    return render(request,'ataprd.html',cont)

def atapr(request,id):
    con=atregdb.objects.filter(id=id).update(status=1)
    return redirect('ata')

def atd(request):
    con=atregdb.objects.filter(status=2)
    cont={
        'inf':con
    }
    return render(request,'atdec.html',cont)

def atdec(request,id):
    con=atregdb.objects.filter(id=id).update(status=2)
    return redirect('atd')

# Apn reqs

def pbks(request):
    con=psyapn.objects.all()
    cont={
        'inf':con
    }
    return render(request,'pbks.html',cont)

def abks(request):
    con=atapn.objects.all()
    cont={
        'inf':con
    }
    return render(request,'abks.html',cont)

#search

#def wsea(request):
    wr=bldb.objects.all()
    li=[wr]
    

