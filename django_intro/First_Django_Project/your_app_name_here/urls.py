from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root_method),
    path('blog', views.index), 
    path('blog/create', views.new),	
    path('blog/<int:number>',views.show), 
    path('blog/<int:number>/edit',views.edit), 
    path('blog/<int:number>/delete',views.destroy),
    path('blog/json',views.redirected_method)
]
