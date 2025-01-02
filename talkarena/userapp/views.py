from django.shortcuts import render,redirect
from.models import *
from adminapp.models import *
from authapp.models import *
from psyapp.models import *
from chat.views import *
# Create your views here.

def ui(request):
    psy=pregdb.objects.filter(status=1)
    auth=atregdb.objects.filter(status=1)
    cont={
        'p':psy,
        'a':auth
    }
    return render(request,'uindx.html',cont)

def abt(request):
    return render(request,'abt.html')

def log(request):
    return render(request,'log.html')

def reg(request):
    return render(request,'reg.html')

def regdata(request):
    if request.method=='POST':
        uname=request.POST['un']
        umail=request.POST['um']
        uprf=request.FILES['uf']
        upsw=request.POST['up']
        data=regdb(uname=uname,umail=umail,uprf=uprf,upsw=upsw)
        data.save()
    return redirect('log')

def logdata(request):
    if request.method == "POST":
        uname=request.POST.get('un')
        upsw=request.POST.get('up')
        if regdb.objects.filter(uname=uname,upsw=upsw).exists():
           data = regdb.objects.filter(uname=uname,upsw=upsw).values('id','umail').first()
           request.session['u_id'] = data['id']
           request.session['email_u'] = data['umail'] 
           request.session['username_u'] = uname
           request.session['password_u'] = upsw
           return redirect('ui') 
        else:
            return render(request,'log.html',{'msg':'invalid user credentials'})
    else:
        return redirect('log')

def logout(request):
    del request.session['u_id']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('log')

def cont(request):
    return render(request,'cont.html')

def contdata(request):
    if request.method=='POST':
        name=request.POST['cn']
        mail=request.POST['ce']
        sub=request.POST['cs']
        msg=request.POST['cm']
        data=contdb(cname=name,cmail=mail,csub=sub,cmsg=msg)
        data.save()
    return redirect('cont')

#cards an single

def pcrd(request):
    pc=pregdb.objects.filter(status=1)
    cont={
        'p':pc
    }
    return render(request,'pcrd.html',cont)

def acrd(request):
    ac=atregdb.objects.filter(status=1)
    cont={
        'a':ac
    }
    return render(request,'acrd.html',cont)

def psng(request,pd):
    if 'u_id' in request.session:
        ps=pregdb.objects.filter(id=pd)
        cont={
            'p':ps
        }
    else:
        return redirect('log')
    return render(request,'psng.html',cont)

def asng(request,ad):
    if 'u_id' in request.session:
        ats=atregdb.objects.filter(id=ad)
        cont={
            'a':ats
        }
    else:
        return redirect('log')
    return render(request,'asng.html',cont)

# apnts 

def papnt(request,id):
    pa=pregdb.objects.filter(id=id)
    cont={
        'p':pa
    }
    return render(request,'papnt.html',cont)

def papndata(request,id):
    if request.method=='POST':
        usrid=request.session.get('u_id')
        num=request.POST['pn']
        sub=request.POST['ps']
        dte=request.POST['pd']
        tme=request.POST['pt']
        data=psyapn(uid=regdb.objects.get(id=usrid),pid=pregdb.objects.get(id=id),num=num,sub=sub,dte=dte,tme=tme)
        data.save()
    return redirect('papntst')

def papntst(request):
    u=request.session.get('u_id')
    pst=psyapn.objects.filter(uid=u)
    cont={
        'st':pst
    }
    request.session['previous_path'] = request.path
    print(request.session['previous_path'])
    return render(request,'papntst.html',cont)

def atapnt(request,id):
    ata=atregdb.objects.filter(id=id)
    cont={
        'a':ata
    }
    return render(request,'atapnt.html',cont)

def atapndata(request,id):
    if request.method=='POST':
        usrid=request.session.get('u_id')
        num=request.POST['an']
        sub=request.POST['as']
        dte=request.POST['ad']
        tme=request.POST['at']
        data=atapn(uid=regdb.objects.get(id=usrid),aid=atregdb.objects.get(id=id),num=num,sub=sub,dte=dte,tme=tme)
        data.save()
    return redirect('atapntst')

def atapntst(request):
    u=request.session.get('u_id')
    ast=atapn.objects.filter(uid=u)
    cont={
        'st':ast
    }
    return render(request,'atapntst.html',cont)

#exp share

def uexp(request):
    ut=topic.objects.all()
    
    cont={
        'ut':ut
    }
    return render(request,'uexp.html',cont)

def ufrm(request):
    return render(request,'uexpfrm.html')

def ufrmdata(request):
    if request.method=='POST':
        usrid=request.session.get('u_id')
        top=request.POST['tn']
        data=topic(uid=regdb.objects.get(id=usrid),top=top)
        data.save()
    return redirect('uexp')

def uexprep(request,id):
    urep=topic.objects.filter(id=id)
    cont={
        'u':urep
    }
    return render(request,'uexprep.html',cont)
        
def repdata(request,id):
    if request.method=='POST':
        rep=request.POST['rp']
        data=reply(did=topic.objects.get(id=id),rep=rep)
        data.save()
    return redirect('ureps', id)        

def ureps(request,id):
    ut=topic.objects.filter(id=id)
    ur=reply.objects.filter(did=id)
    cont={
        'ut':ut,'ur':ur
    }
    return render(request,'ureps.html',cont)

