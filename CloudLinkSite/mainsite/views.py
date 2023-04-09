from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User
# Create your views here.


def overview_page(request):
    return render(request, 'overview.html')

def registration_page(request):
    return render(request, 'registration.html')

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def services_page(request):
    return render(request, 'service.html')

def contact_page(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        data = User(username=username, password=password, email=email, firstname=firstname, lastname=lastname,
                    address1=address1, address2=address2, city=city, state=state, zip=zip, phone=phone)
        data.save()
    return redirect('/signin/')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            return redirect('/home')
        else:
            return HttpResponse('incorrect Password')
    except:
        return HttpResponse('No user registered under that name')

def dashboard(request):
    return render(request, 'dashboard.html')

def myspace(request):
    return render(request, 'myspace.html')

def account(request):
    return render(request, 'account.html')

def billing(request):
    return render(request, 'billing.html')

def support(request):
    return render(request, 'support.html')