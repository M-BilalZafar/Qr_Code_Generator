from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_page,name='login'),

    path('home/', views.index,name='home'),
    path('logout/', views.logout_logg,name='logout'),
]