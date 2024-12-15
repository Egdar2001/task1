from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'app2_index'),
    path('home', views.home, name='app2_home'),
]