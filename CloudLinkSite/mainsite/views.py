from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import User
import hashlib
# Create your views here.


def overview_page(request):
    return render(request, 'overview.html')

def registration_page(request):
    return render(request, 'registration.html')

def about_page(request):
    return render(request, 'about.html')

def services_page(request):
    return render(request, 'service.html')

def contact_page(request):
    return render(request, 'contact.html')

def home_page(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}
        request.session["user.id"]

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    except:
        return redirect("/login/")
    return render(request, 'index.html', context)

def dashboard(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'dashboard.html', context)

def myspace(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'myspace.html', context)

def account(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'account.html', context)

def billing(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'billing.html', context)

def support(request, username):
    try:
        user = User.objects.get(username=username)
        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'support.html', context)

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
    print(password)
    password = hashlib.sha256(password.encode()).hexdigest()
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            request.session[f'{user.id}'] = user.username
            return HttpResponseRedirect(reverse("cloud:home", args=(user.username, )))
        else:
            return HttpResponse('incorrect Password')
    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

def logout(request, id):
    del request.session[f"{id}"]

def update_ac_details(request, username):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        user = User.objects.get(username=username)

        user.email = email
        user.firstname = firstname
        user.lastname = lastname
        user.address1 = address1
        user.address2 = address2
        user.city = city
        user.state = state
        user.zip = zip
        user.phone = phone
        user.save()
        # except:
        #     raise Http404(f"The Username {username} is not available!")

    return HttpResponseRedirect(reverse("cloud:account", args=(username, )))