from django.contrib import admin
from django.urls import path, include
from .views import register
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
	path('register/',register, name ='register'),	
    path('login/', auth_views.LoginView.as_view(), name='login') ,
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout') ,
]
