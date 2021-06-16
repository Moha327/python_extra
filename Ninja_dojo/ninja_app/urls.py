from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('ab', views.add_dojo),
    path('cd',views.add_ninja)
    # path('adddojo', views.add_dojo),
    # path('add_ninja',views.add_ninja)

]