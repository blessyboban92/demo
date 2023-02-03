from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credential")
            return redirect('login')
    return render(request,'login.html')


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname= request.POST['first_name']
        lname = request.POST['last_name']
        email_id = request.POST['email_id']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Alreay existed user")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,"Your email_id is incorrect")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email_id,password=password)
                user.save();
                return redirect('login')
            print("User Created")
        else:
            messages.info(request,"Password does not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
