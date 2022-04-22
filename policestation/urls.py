from django.urls import path
from policestation import views

urlpatterns = [

    path('',views.commissioner_login,name='commissioner-login'),
    path('home/',views.home,name='home'),
    path('add-inspector/',views.add_inspector,name='add-inspector'),
    path('view-inspectors/',views.view_inspectors,name='view-inspectors'),
    path('inspector-update/<int:pk>',views.inspector_update,name='inspector-update'),
    path('delete-inspector/<int:pk>',views.delete_inspector,name='delete-inspector'),
    path('add-constable/',views.add_constable,name='add-constable'),
    path('constable-update/<int:pk>',views.constable_update,name='constable-update'),
    path('delete-constable/<int:pk>',views.delete_constable,name='delete-constable'),
    path('view-constables/',views.view_constables,name='view-constables'),
    path('manageinfo/',views.manageinfo,name='manageinfo'),
    path('addinfo/',views.addinfo,name='addinfo'),
    path('manageinfo-update/<int:pk>',views.manageinfo_update,name='manageinfo-update'),
    path('delete-info/<int:pk>',views.delete_info,name='delete-info'),
    path('completed-action/<int:pk>',views.completed_action,name='completed-action'),
    path('action-completed/<int:pk>',views.action_completed,name='action-completed'),
    path('log-out/',views.log_out,name='log-out'),
    path('forgot-password/',views.log_out,name='forgot-password'),
    path('firs/',views.firs,name='firs'),
    path('complaints/',views.complaints,name='complaints'),
]