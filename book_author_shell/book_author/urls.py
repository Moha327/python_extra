from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('books/<int:id1>',views.display), 
    path('book/<int:id1>',views.add),
    path('author',views.index3),
    path('author/<int:id1>',views.add2),
    path('author/<int:id1>',views.add3),
] 
# path      views.index     addbook   views.addBook                shows/<int:id> views.showBook