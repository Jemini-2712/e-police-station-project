from . import views
from django.urls import path

urlpatterns = [

    path('',views.inspector_login,name='inspector-login'), 
    path('first/',views.first,name='first'),
    path('show-fir/',views.show_fir,name='show-fir'), 
    path('show-complaints/',views.show_complaints,name='show-complaints'), 
    # path('pending/<int:pk>',views.pending,name='pending'), 
    # path('completed/<int:pk>',views.completed,name='completed'), 
    path('sign-out/',views.sign_out,name='sign-out'), 

]