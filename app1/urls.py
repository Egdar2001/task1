from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'app1_index'),
    path('home', views.home, name='app1_home'),
]