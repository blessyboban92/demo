from django.http import  HttpResponse
from django.shortcuts import render

from .models import Place, Meet


# Create your views here.
#def index(request):
    #return render(request, "about.html")

def demof(request):
    obj=Place.objects.all()
    obj1 = Meet.objects.all()
    return render(request,"index.html",{'result':obj,'meetresult':obj1})

def about(request):
    return render(request,"about.html")

#def operation(request):
    #   x=int(request.GET['number1'])
    #y=int(request.GET['number2'])
    #SUM=x+y
    #diff=x-y
    # product=x*y
    #Quotient=x/y
    #return render(request,"result.html",{'result1':SUM,'result2':diff,'result3':product,'result4':Quotient})