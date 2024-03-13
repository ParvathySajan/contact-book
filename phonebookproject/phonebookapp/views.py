from django.shortcuts import render
from.models import Phonebook

# Create your views here.
def home(request):
    return render(request,'index.html')

def addcontact(request):
    response={}
    try:
        na=request.POST['cname']
        ph=int(request.POST['num'])
        phdtls=Phonebook.objects.filter(name=na)
        if phdtls.exists():
            response['msg']='Contact already exist'
            return render(request,'index.html',response)
        else:
            phlist=Phonebook(name=na,phone=ph)
            phlist.save()
        response['msg']='Contact Added'
        return render(request,'index.html',response)
    except Exception as e:
        print(e)
        response['msg']='Contact Not Added'
        return render(request,'index.html',response)

def display(request):
    phdtls=Phonebook.objects.all()
    return render(request,'index.html',{'pb':phdtls})

def delete(request):
    response={}
    try:
        delname=request.POST['dname']
        phdtls=Phonebook.objects.filter(name=delname)
        phdtls.delete()
        return render(request,'index.html',{'dmsg':'Contact Deleted'})
    except Exception as e:
        print(e)
        return render(request,'index.html',{'dmsg':'Contact Not Deleted'})
        
def update(request):
    response={}
    field=request.POST['naph']
    try:
        if field=='name':
            oldname=request.POST['old'] 
            newname=request.POST['new']
            phdtls=Phonebook.objects.filter(name=newname)
            if phdtls.exists():
                response['upmsg']='Name already exist'
                return render(request,'index.html',response)
            else:
                Phonebook.objects.filter(name=oldname).update(name=newname)
            return render(request, 'index.html',{'upmsg':'Updated'})
        elif field=='phone':
            nameph=request.POST['old2']
            newphone=int(request.POST['newph'])
            Phonebook.objects.filter(name=nameph).update(phone=newphone)
            return render(request, 'index.html',{'upmsg':'Updated'})

    except Exception as e:
            print(e)
            return render(request,'index.html',{'upmsg':'Not Updated'})
    
    















'''def updates(request):
    response={}
    try:
        nameph=request.POST['old2']
        newphone=int(request.POST['newph'])
        Phonebook.objects.filter(name=nameph).update(phone=newphone)
        return render(request, 'index.html',{'umsg':'Updated'})
    except Exception as e:
        print(e)
        return render(request,'index.html',{'umsg':'Not Updated'})'''
        
    





