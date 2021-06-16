from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('welcome',views.welcome),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('delete/<int:id>',views.delete),
    path('user/<int:id>',views.profile)
]