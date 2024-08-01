from django.contrib import admin
from django.urls import path,include
from traveluser import views
urlpatterns = [

    path('', views.user_indexview,name='user_index'),
    path('about/', views.user_about,name='about'),
    path('service/', views.user_service,name='service'),
    path('contact/', views.user_contact,name='contact'),
    path('destination/',views.user_destination,name='destination'),
    path('package/',views.user_packages,name='package'),

    path('my_booking/',views.user_booking,name='my_booking'),
    path('testimonial/',views.user_testimonial,name='testimonial'),
    path('team/',views.user_team,name='team'),
    path('package_detail/<int:id>/',views.package_detail,name='package_detail'),
    path('book_packages/<int:id>/',views.book_packages,name='book_packages'),

    path('register/',views.user_register,name='register'),
    path('loginview/',views.loginview,name='loginview'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('payment/<int:id>/',views.user_payment,name='payment'),
    path('confirmed/<int:id>/',views.confirmed,name='confirmed'),
    path('bookingdetail/',views.bookingdetail,name='bookingdetail'),
    # path('generate-pdf/', views.generate_pdf, name='generate_pdf'),

    path('packagesearch/',views.packagesearch,name='packagesearch'),


        
]