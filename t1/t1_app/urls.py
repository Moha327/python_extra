from django.urls import path
from . import views
urlpatterns = [
path('',views.index),
path('base',views.index2),
path('base2',views.index2)
]