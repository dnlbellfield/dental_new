from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('new_index/', views.new_index, name='new_index'),

    ]