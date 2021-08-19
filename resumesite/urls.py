from django.urls import path
from . import views


urlpatterns = [
    path('sam/', views.home, name="sam"),
   
]