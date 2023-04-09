from django.urls import path
from . import views

app_name = 'cloud'
urlpatterns = [
    path('', views.overview_page, name='overview'),
    path('services/', views.services_page, name='services'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('<str:username>/home/', views.home_page, name='home'),
    path('<str:username>/dashboard/', views.dashboard, name='dashboard'),
    path('<str:username>/myspace/', views.myspace, name='myspace'),
    path('<str:username>/account/', views.account, name='account'),
    path('<str:username>/billing/', views.billing, name='billing'),
    path('<str:username>/support/', views.support, name='support'),
    path('login/', views.login, name='login'),
    path('signin/', views.registration_page, name='signin'),
    path('register/', views.register, name='register'),
    path('update/', views.update_ac_details, name='update')
]