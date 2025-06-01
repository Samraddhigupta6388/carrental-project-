"""
URL configuration for carrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carrental import views
from django.conf.urls.static import static
from django.conf import settings
from .views import update_verification


urlpatterns = [
    path("update_verification/", update_verification, name="update_verification"),
  
    path('admin/', admin.site.urls),
    path('first/',views.first,name='first'),
    path('second/',views.second,name='second'),
    path('index/',views.index,name='index'),
    path('',views.home,name='home'),
    path('layout/',views.layout,name='layout'),
    path('logout/',views.logout,name='logout'),
    path('homelogin/',views.homelogin,name='login'),
    # path('savelogindetail/',views.savelogindetail,name='savelogindetail'),
    path('registration_view/',views.registration_view,name='registration_view'),
    # path('saveregistration/',views.saveregistration,name='saveregistration'),
    path('savepost_v/',views.savepost_v,name="savepost_v"),
    path('contact/',views.contact,name='contact'),
    path('savecontact',views.savecontact,name="savecontact"),
    path('explore/',views.explore,name="explore"),
    path('admindash/',views.admindash,name="admindash"),
    path('managereg/',views.managereg,name='managereg'),
    path('managebk/',views.managebk,name='managebk'),
    path('paymentD/<int:car_id>/', views.paymentD, name='paymentD'),    
    path('postvehicle/',views.postvehicle,name='postvehicle'),
    path('vehiclemanage/',views.vehiclemanage,name='vehiclemanage'),
    path('manageCQ/',views.manageCQ,name='manageCQ'),
    path('msgDL/',views.msgDL,name="msgDL"),
    path('verifyform/',views.verifyform,name="verifyform"),
    path('saveveriform/',views.saveveriform,name="saveveriform"),
    path('verify/<path:email>/', views.verify, name='verify'),
    path('deleteCQ/<int:id>/',views.deleteCQ,name='deleteCQ'),
    path('deletecar/<int:id>/',views.deletecar,name='deletecar'),
    path('deleteuser/<int:id>/',views.deleteuser,name='deleteuser'),
    path('deletemanagebk/<int:id>/', views.deletemanagebk, name='deletemanagebk'),
    path('deletereg/<str:useremail>/',views.deletereg,name='deletereg'),
    path('paystatus/',views.paystatus,name="paystatus"),
    path('user_verify/',views.user_verify, name='user_verify'),
    path('payment/<int:id>/',views.payment,name="payment"),
    path('car/<int:car_id>/', views.car, name='car'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('update_verification/',views.update_verification,name="update_verification"),
    path('create_order/',views.create_order, name='create_order'),
    path('update_booking_status/',views.update_booking_status,name='update_booking_status'),
    path('payment_success/',views.payment_success,name="payment_success"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#static used to import media   
