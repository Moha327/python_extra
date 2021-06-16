from django.urls import path
from.import views
urlpatterns = [
    path('',views.index),  
    path('welcome',views.welcome), 
    path('register',views.register),
    path('logout',views.logout),
    path('login',views.login) ,
     path('add_book',views.add_book)   
]
    