from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('create',views.createuser),
    path('welcome',views.welc),
    path('login',views.login),
    path('logout',views.logout),
    path('addBook/<int:id>',views.addBook),
    path('deleteBook/<int:id>',views.deleteBook),
    path('showbook/<int:id>',views.showFave),
    path('addFavarit/<int:id>',views.addFavarit),
    path('updatedes/<int:id>', views.updatedes),
    path('deletedes',views.deletedes),
    path('unfavarit/<int:id>',views.unfavarit)
    
]