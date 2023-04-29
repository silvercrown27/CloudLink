from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'cloud'
urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myspace/', views.myspace, name='myspace'),
    path('account/', views.account, name='account'),
    path('billing/', views.billing, name='billing'),
    path('support/', views.support, name='support'),
    path('<int:id>/', views.signout, name='signout'),
    path('update/<str:username>/', views.update_ac_details, name='update')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)