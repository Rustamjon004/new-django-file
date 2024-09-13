from django.urls import path

from . import views

urlpatterns = [

    path('', views.home_page),


    path('login/', views.login_page),


    path('logout/', views.logout_page),


    path('registration/', views.registration_page),
]

