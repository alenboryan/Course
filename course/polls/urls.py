from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_info", views.all_info, name="all_info")
    
]

