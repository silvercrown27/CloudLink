import hashlib

from .models import User

from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def overview_page(request):
    return render(request, 'overview.html')

def registration_page(request):
    return render(request, 'registration.html')

def about_page(request):
    return render(request, 'about.html')

def services_page(request):
    return render(request, 'services.html')

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

        password = hashlib.sha256(password.encode()).hexdigest()

        data = User(username=username, password=password, email=email, firstname=firstname, lastname=lastname,
                    address1=address1, address2=address2, city=city, state=state, zip=zip, phone=phone)
        data.save()

    return redirect('/signin/')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password = hashlib.sha256(password.encode()).hexdigest()
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            request.session['user_id'] = user.id
            return redirect(f"/{username}/home/")
        else:
            return HttpResponse('incorrect Password')
    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")