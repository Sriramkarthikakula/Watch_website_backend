from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def logins(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Login Credentials are wrong!")
            return redirect('logins')
    else:
        return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        last_name = request.POST['last_name']
        email = request.POST['email']
        repass = request.POST['repass']
        if password==repass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Taken")
                return redirect('signup')
            else:  
                user = User.objects.create_user(username=username,password=password,last_name=last_name,email=email)
                user.save()
                user = auth.authenticate(username=username,password=password)
                if user is not None :
                    auth.login(request,user)
                    return redirect('/')
        else:
            messages.info(request,"Password not match")
            return redirect('signup')
    else:
        return render(request,'reg.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def adminlog(request):
    objs=User.objects.all()
    return render(request,'adminlog.html',{'obj':objs})

def admin(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('intercall1')
        else:
            messages.info(request,"Your Not an admin")
            return redirect('admin')
    else:
        return render(request,'adminlogin.html')
    
def intercall1(request):
    return render(request,'intermed.html')

def inter(request):
    n6 = request.POST['n6']
    print(n6)
    if (n6 == "True"):
        return redirect('adminlog')
    else:
        messages.info(request,"invalid credentials")
        return redirect('admin')