from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('', views.overview_page, name='overview'),
    path('services/', views.services_page, name='services'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', views.login, name='login'),
    path('signin/', views.registration_page, name='signin'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myspace/', views.myspace, name='myspace'),
    path('account/', views.account, name='account'),
    path('billing/', views.billing, name='billing'),
    path('support/', views.support, name='support'),
]