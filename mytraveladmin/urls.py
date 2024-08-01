from django.contrib import admin
from django.urls import path
from mytraveladmin import views

urlpatterns=[
    
    path('admin_index/', views.admin_indexview, name='admin_index'),
    path('dashboard/',views.admin_dashview,name='dashboard'),

    path('sign_in/',views.admin_sign_in,name='sign_in'),
    path('logoutview/',views.admin_logoutview,name='logoutview'),
    path('admin_sign_up/',views.admin_sign_up,name='admin_sign_up'),
   
    path('tables/',views.admin_tables,name='tables'),
    path('taskdelete/<int:id>/',views.admin_delete,name='taskdelete'),
    path('taskedit/<int:id>/',views.admin_edit,name='taskedit'),
    path('taskupdate/<int:id>/',views.admin_update,name='taskupdate'),
    path('form/',views.admin_form,name='form'),
    
    
    # pakages
    path('tables1/',views.admin_tables1,name='tables1'),
    path('form1/',views.admin_form1,name='form1'),
    path('packagesdelete/<int:id>/',views.admin_packagesdelete,name='packagesdelete'),
    path('packagesedit/<int:id>/',views.admin_packagesedit,name='packagesedit'),
    path('packagesupdate/<int:id>/',views.admin_packagesupdate,name='packagesupdate'),
]