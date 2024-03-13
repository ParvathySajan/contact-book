from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('add',views.addcontact),
    path('disp',views.display),
    path('del',views.delete),
    path('upname',views.update),
    
    
]