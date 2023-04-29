from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.conf import settings

from mainsite.models import User

import hashlib
import os

# Create your views here.
def home_page(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        # Add a context dictionary and a directory path then add the paths of
        # all image files in the directory to the context under the key 'image_paths'.

        image_paths = []
        for filename in os.listdir(settings.MEDIA_ROOT):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                path = os.path.join('img', filename)
                image_paths.append(path)
        context = {'user': user, 'image_paths': image_paths}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'index.html', context)


def dashboard(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'dashboard.html', context)

def myspace(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'myspace.html', context)

def account(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'account.html', context)

def billing(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'billing.html', context)

def support(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        context = {"user": user}

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")

    return render(request, 'support.html', context)

def signout(request, id):
    user = User.objects.get(id=id)
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect("/signin/")
    else:
        print("No session found")


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

    return HttpResponseRedirect(reverse("cloud:account", args=(username, )))
