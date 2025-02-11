from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method =='POST':
        email= request.POST['email']
        password= request.POST['password']
        confirmpassword= request.POST['confirmpassword']
        if password!= confirmpassword:
            messages.error(request,"password is not matching")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"email already exist")
                # return HttpResponse("email already exist")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active=True
        user.save()
        
        messages.info(request,"User created successfully",)
        return redirect ('/auth/login')
            

    
    return render(request,"signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword= request.POST['password']
        myuser= authenticate(username=username,password=userpassword)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'login Success')
            return redirect("/")
        else:
            messages.error(request,"invalid credentials")
            return redirect('/auth/login')

    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    
    messages.success(request,"logout Success")
    return redirect('/')