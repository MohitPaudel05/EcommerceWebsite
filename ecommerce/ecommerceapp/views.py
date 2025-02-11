from django.shortcuts import render ,HttpResponse
from ecommerceapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        phonenumber=request.POST.get("phonenumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=phonenumber)
        # myquery=Contact(name=name,desc=desc,phonenumber=phonenumber)
        myquery.save()
        messages.info(request," we will get back to you soon")
        return render(request, "contact.html")

    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")