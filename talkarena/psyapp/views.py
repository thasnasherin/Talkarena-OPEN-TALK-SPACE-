from django.shortcuts import render,redirect
from.models import*
from userapp.models import*
from chat.views import*
import uuid

# Create your views here.
def pi(request):
    p=request.session.get('p_id')
    ps=pregdb.objects.filter(id=p)
    cont={
        'x':ps,
    }
    psy=pregdb.objects.filter(status=1).count()
    bk=psyapn.objects.filter(status=0).count()
    aprbk=psyapn.objects.filter(status=1).count()
    dclnbk=psyapn.objects.filter(status=2).count()
    return render(request,'psyindx.html',cont,{'aprbk':aprbk,'psy':psy,'dclnbk':dclnbk,'bk':bk})

def preg(request):
    return render(request,'psyreg.html')

def plog(request):
    return render(request,'psylog.html')

def pregdata(request):
    if request.method=='POST':
        pname=request.POST['pn']
        pmail=request.POST['pe']
        pqual=request.POST['pq']
        pexp=request.POST['pex']
        pgen=request.POST['pg']
        pprf=request.FILES['pid']
        ppsw=request.POST['pp']
        data=pregdb(pname=pname,pmail=pmail,pqual=pqual,pexp=pexp,pgen=pgen,pprf=pprf,ppsw=ppsw)
        data.save()
    return redirect('plog')

def plogdata(request):
    if request.method == "POST":
        pname=request.POST.get('pn')
        ppsw=request.POST.get('pp')
        if pregdb.objects.filter(pname=pname,ppsw=ppsw).exists():
           data = pregdb.objects.filter(pname=pname,ppsw=ppsw).values('id','pmail','pqual','pexp','pgen').first()
           request.session['p_id'] = data['id']
           request.session['email_p'] = data['pmail']
           request.session['qual_p'] = data['pqual']
           request.session['exp_p'] = data['pexp']
           request.session['gen_p'] = data['pgen']
           request.session['username_p'] = pname
           request.session['password_p'] = ppsw
           return redirect('pi') 
        else:
            return render(request,'psylog.html',{'msg':'invalid user credentials'})
    else:
        return redirect('plog')

def plogout(request):
    del request.session['p_id']
    del request.session['email_p']
    del request.session['qual_p']
    del request.session['exp_p']
    del request.session['gen_p']
    del request.session['username_p']
    del request.session['password_p']
    return redirect('pi')

def paprs(request):
    p=request.session.get('p_id')
    pa=pregdb.objects.filter(status=1,id=p)
    cont={
        'p':pa
    }
    return render(request,'paprs.html',cont)

def pdecs(request):
    p=request.session.get('p_id')
    pd=pregdb.objects.filter(status=2,id=p)
    cont={
        'p':pd
    }
    return render(request,'pdecs.html',cont)


#apnts reqs

def apnreq(request):
    p=request.session.get('p_id')
    con=psyapn.objects.filter(status=0,pid=p)
    cont={
        'inf':con
    }
    return render(request,'apnreqs.html',cont)

def apna(request):
    p=request.session.get('p_id')
    
    con=psyapn.objects.filter(status=1,pid=p)
    
    request.session['previous_path'] = request.path

    cont={
        'inf':con
    }
    return render(request,'apnapr.html',cont)

def apnapr(request,id):
    generated_room_id = uuid.uuid4()
    con=psyapn.objects.filter(id=id).update(status=1, rid = generated_room_id)
    return redirect('apna')

def apnd(request):
    p=request.session.get('p_id')
    con=psyapn.objects.filter(status=2,pid=p)
    cont={
        'inf':con
    }
    return render(request,'apndec.html',cont)

def apndec(request,id):
    con=psyapn.objects.filter(id=id).update(status=2)
    return redirect('apnd')

