from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'usersite'
urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myspace/', views.myspace, name='myspace'),
    path('account/', views.account, name='account'),
    path('billing/', views.billing, name='billing'),
    path('support/', views.support, name='support'),
    path('signout/', views.signout, name='signout'),
    path('update/', views.update_ac_details, name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)