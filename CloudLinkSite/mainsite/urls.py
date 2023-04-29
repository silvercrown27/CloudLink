from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.overview_page, name='overview'),
    path('services/', views.services_page, name='services'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', views.login, name='login'),
    path('signin/', views.registration_page, name='signin'),
    path('register/', views.register, name='register'),
]
