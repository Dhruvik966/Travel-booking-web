from django.contrib import admin 
from django.urls import path, include
from api import views


urlpatterns = [

    path('index/',views.index),
    path('sign_in/',views.admin_sign_in,name='sign_in'),
    path('admin_sign_up/',views.admin_sign_up,name='admin_sign_up'),
    path('taskedit/',views.admin_edit,name='taskedit'),
    path('taskupdate/<int:id>/',views.admin_update,name='taskupdate'),

    path('additem/',views.additem,name='additem'),
    path('deleteitem/<int:id>/',views.deleteitem,name='deleteitem'),

    
    path('',views.admin_form,name='form'),
    

]