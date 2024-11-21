from django.contrib import admin
from django.urls import path
from Google_Authentication import views


urlpatterns = [
    path('home/', views.home,name='homepage'),
    path('postlogin/',views.Post_login, name='postlogin'),
    path('sendemail/',views.send_email, name='sendemail'),
    path('adminpage/',views.Admin_Page, name='adminpage'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('addTask/', views.Add_Task, name='add_task'),
    path('updateTask/<int:pk>/',views.Update_Task, name='update_task'),
    path('deleteTask/<int:pk>/', views.Delete_Task, name='delete_task'),
    
]