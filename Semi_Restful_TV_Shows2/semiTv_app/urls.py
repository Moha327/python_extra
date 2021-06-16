from django.urls import path
from . import views
urlpatterns = [

   path('', views.index),
   path('shows/new', views.show_new),
   path("process_data", views.process_data),
   path('shows/<id>', views.showInfo),
   path('shows/<id>/edit', views.edit),
   path('shows', views.showAll),
]     
