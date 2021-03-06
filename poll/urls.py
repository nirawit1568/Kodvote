from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_poll/', views.add_poll, name='add_poll'),
    path('my_poll/', views.my_poll, name='my_poll'),
    path('save_poll/', views.save_poll, name='save_poll'),
]