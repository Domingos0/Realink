
from django.urls import path
from .views import HomeView, sair 
from django.contrib.auth import views as auth_views
# from django.contrib.auth.models import User
""" from django.conf.urls import url """


urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', sair, name='logout'),
    

] 

    