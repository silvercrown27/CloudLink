import hashlib

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from usersite.models import Drives, Folders
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


@receiver(post_save, sender=User)
def create_user_drive(sender, instance, created, **kwargs):
    if created:
        create_main_drive(instance.username)

def create_main_drive(username):
    name = "My Drive C"
    user = User.objects.get(username=username)
    capacity = 5000000

    drive = Drives.objects.create(drive_name=name, drive_user=user, capacity=capacity)

    fname = "MyDesktop"
    Folders.objects.create(name=fname, path=f"/{name}/MyDesktop/", drive_id=drive)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        password = hashlib.sha256(password.encode()).hexdigest()

        User.objects.create(
            username=username, password=password, email=email, first_name=firstname, last_name=lastname,
            address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, phone=phone
        )

    return redirect('/signin/')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password = hashlib.sha256(password.encode()).hexdigest()
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            request.session['user_id'] = user.id
            url = reverse('usersite:home', args=[username])
            return redirect(url)
        else:
            return HttpResponse('incorrect Password')
    except User.DoesNotExist:
        raise Http404(f"No user registered under the name {username}")