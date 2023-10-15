from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
   
    # path('signin/', views.googleSignin, name="login"),
    path('', views.register, name="register"),
    path('accounts/login/', views.login_attempt, name="signin"),
    path('accounts/profile/', views.profile, name="profile"),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]