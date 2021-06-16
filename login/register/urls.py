from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),  
    # path('welcome',views.welcome), 
    path('register',views.add),
     path('login',views.login),
    path('success',views.success),
    path('logout',views.logout),
]
