from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginuser/", views.loginuser, name="loginuser"),
    path("homepageuser/<str:Studentname>/",views.homepageuser, name="homepageuser"),

    path("event1/", views.event1, name="event1"),
    path("event2/", views.event2, name="event2"),
    
    path("booking1/", views.booking1, name="booking1"),
    path("booking2/", views.booking2, name="booking2"),
    path("booking3/", views.booking3, name="booking3"),
    path("booking4/", views.booking4, name="booking4"),
    path("viewbooking/", views.viewbooking, name="viewbooking"),
    path('viewbooking/delete/<str:bookingid>', views.delete_bookingpage, name='delete'),


    path("loginadmin/", views.loginadmin, name="loginadmin"),
    path("adminhomepage/<str:Adminid>/",views.adminhomepage, name="adminhomepage"),
    path("addevent/",views.addevent, name="addevent"),
    path("viewdeleteevent/",views.viewdeleteevent, name="viewdeleteevent"),
    path('viewdeleteevent/delete/<str:Eventname>', views.delete_eventpage, name='delete'),
    path("addfacility/",views.addfacility, name="addfacility"),
    path("viewdeletefacility/",views.viewdeletefacility, name="viewdeletefacility"),
    path('viewdeletefacility/delete/<str:Facilityname>', views.delete_facilitypage, name='delete'),
    path("viewevent/",views.viewevent, name="viewevent"),
    path("viewfacility/",views.viewfacility, name="viewfacility"),

    
]