from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('citizen-login/',views.citizen_login,name='citizen-login'),
    path('citizen-dashboard1/',views.citizen_dashboard,name='citizen-dashboard1'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('f-password/',views.f_password,name='f-password'),
    path('change-password/',views.change_password,name='change-password'),
    path('addfir/',views.addfir,name='addfir'),
    path('addcomplaint/',views.addcomplaint,name='addcomplaint'),
    path('feedback/',views.feedback,name='feedback'),
    path('viewfir/',views.viewfir,name='viewfir'),
    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('logout/',views.logout,name='logout'),
    path('policestations/',views.policestations,name='policestations'),

]