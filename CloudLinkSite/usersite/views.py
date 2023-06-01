import os

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.conf import settings
from django.http import Http404
from django.urls import reverse

from .models import Drives, Folders, Files
from mainsite.models import User


def calculate_drive_size(drive_id):
    total_size = Files.objects.filter(drive_id=drive_id).aggregate(Sum('file_size'))['file_size__sum']
    return total_size if total_size else 0


###### functions to create drives, and input data into tables ######

def new_drive(drive_name, user_name, capacity):
    drive_user = User.objects.get(username=user_name)

    if capacity <= User.object.get(username=user_name).allocated_space:
        Drives.objects.create(drive_name=drive_name, drive_user=drive_user, capacity=capacity)
        print(f"New drive {drive_name} created successfully!")
    else:
        print(f"The capacity ({capacity}) exceeds the allocated space for user {user_name}"
              f" ({drive_user.allocated_space}).")


def exists(model, drive_id, path):
    try:
        md = model.objects.filter(drive_id=drive_id, path=path)
        return True

    except md.DoesNotExist:
        return False


def add_folder(name, path, drive_id):
    Folders.objects.create(name=name, path=path, drive_id=drive_id)


def add_file(name, path, ext, folder_id, drive_id, size):
    if calculate_drive_size(drive_id) > size:
        Files.objects.create(name=name, path=path, file_ext=ext, folder_id=folder_id, drive_id=drive_id, file_size=size)


def get_size(filepath):
    with open(filepath, 'rb') as f:
        size = len(f) / (1024 ** 2)
        return size


def add_file_info_to_db(folder_id, drive_id, file):
    file_name = os.path.splitext(file[0])
    file_size = get_size(file)
    extension = os.path.splitext(file)[1]
    folder_id = folder_id
    drive_id = drive_id
    add_file(file_name, file, extension, folder_id, drive_id, file_size)


def remove_media_root(file_paths):
    media_root = settings.MEDIA_ROOT
    len_mr = len(media_root)

    return file_paths[len_mr + 1:]


def upload(request, username):
    try:
        user = User.objects.get(username=username)
        if request.method == 'POST':
            file_paths = request.POST.getlist('file_paths[]')
            files = request.FILES.getlist('files[]')
            default_path = f"{user.id}/My Desktop"

            # Loop through the files and save them as needed
            for i in range(len(file_paths)):
                print(file_paths[i])
                print(files[i])

            fs = FileSystemStorage()

            for i, file in enumerate(files):
                # construct the file path by combining the folder path and the relative path
                file_path = os.path.join(settings.MEDIA_ROOT, default_path, file_paths[i])
                # save the file to the file system
                fs.save(file_path, file)

        # add_file_info_to_db(folder_id, drive_id, path)
        return redirect("../myspace/")

    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")


def home_page(request, username):
    try:
        user = User.objects.get(username=username)
        if 'user_id' not in request.session:
            return redirect('/signin/')

        media_files = []
        image_extensions = ('.png', '.jpg', '.jfif')
        video_extensions = ('.gif', '.mp4', '.mkv')
        for dirpath, dirname, filenames in os.walk(settings.MEDIA_ROOT):
            for file in filenames:
                if file.endswith(image_extensions + video_extensions):
                    path = os.path.join(remove_media_root(dirpath), file)
                    ext = file.split(".")[1]
                    media_files.append([path, f".{ext}"])

        context = {'user': user, "media_files": media_files, "v_ext": video_extensions, "i_ext": image_extensions}

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
