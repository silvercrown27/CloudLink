import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse

from mainsite.models import User


def upload_folder_to_media_root(folder_path, locs=[]):
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)

    # get the name of the current folder
    folder_name = os.path.basename(folder_path)
    locs.append(folder_name)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isdir(file_path):
            # recursively call this function with updated locs parameter
            upload_folder_to_media_root(file_path, locs)
            # clear the current folder from locs after the recursive call
            locs.pop()
        else:
            # construct the final path for this file
            final_path = os.path.join(*locs, file_name)
            # open the file and save it to the media root
            with open(file_path, 'rb') as f:
                locs.append(os.path.basename(file_path))
                fs.save(final_path, f)
                locs.pop()


def home_page(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        image_paths = []
        for filename in os.listdir(settings.MEDIA_ROOT):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                path = os.path.join('img', filename)
                image_paths.append(path)

        context = {'user': user}
        return render(request, 'index.html', context)

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")


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

        return render(request, "myspace.html", context)

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")


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

def signout(request, username):
    User.objects.get(username=username)
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect("/signin/")
    else:
        print("No session found")


def update_ac_details(request, username):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        user = User.objects.get(username=username)

        user.email = email
        user.first_name = firstname
        user.last_name = lastname
        user.address1 = address1
        user.address2 = address2
        user.city = city
        user.state = state
        user.zip_code = zip_code
        user.phone = phone
        user.save()

    return HttpResponseRedirect(reverse("cloud:account", args=(username,)))
