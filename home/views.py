from django.shortcuts import render, redirect
from django.http import response
from home import serializer
from rest_framework.response import Response
from .serializer import AccountSerializer
from .models import Account
from rest_framework.decorators import api_view

# Create your views here.
def myCheck(response):
    db=Account.objects.all()
    return render(response,"index.html",{'obj':db})


def myCreate(response):
    if response.method=="POST":
        rstatement=response.POST.get("statement")
        rgrouping=response.POST.get("grouping")
        rgrouping_label=response.POST.get("grouping_label")
        raccount_name=response.POST.get("account_name")
        raccount_name_label=response.POST.get("account_name_label")
        rcontext=response.POST.get("context")
        rvalue=response.POST.get("value")
        runit=response.POST.get("unit")

        if (rstatement!="" and rgrouping!="" and rgrouping_label!="" and raccount_name!="",raccount_name_label!="",rcontext!="",rvalue!="",runit!=""):
            e=Account(statement=rstatement,grouping=rgrouping,grouping_label=rgrouping_label, account_name=raccount_name,account_name_label=raccount_name_label,context=rcontext, value=rvalue,unit=runit)
            e.save()
            return redirect("/")
        else:
            return redirect("/")

def myUpdate2(request,i):
    db=Account.objects.get(id=i)
    return render(request,"dataenter.html",{'db':db})
       
@api_view(['PUT'])       
def myUpdate(response,i):
    print("Spot1")
    if response.method=="PUT":
        db = Account.objects.get(id=i)
        
        serializer=AccountSerializer(instance=db, data=response.data)
        
        print(response.data)

        if serializer.is_valid():
            
            serializer.save()
            print("Data entered")
            return Response("Data Entered")
        else:
            return Response("Data Entered")
    
@api_view(['GET'])
def myCheck1(response):
    db=Account.objects.all()
    serializer=EmployeeSerializer(db,many=True)
    return Response(serializer.data)

def myDelete(response,i):
    obj=Account.objects.get(id=i)
    obj.delete()
    return redirect("/")
    
