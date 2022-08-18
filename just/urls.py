from django.urls import path, include
from django.views import View
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('get/', views.get_details, name='get'),
    path('price/', views.price, name='price'),

]
