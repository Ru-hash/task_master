from django.contrib import admin
from django.urls import path, include
from .views import TaskListView,TaskCreateView,TaskDeleteView


app_name = 'tasks'
urlpatterns = [
	
    path('',TaskListView, name ='TaskList'),
    path('create/',TaskCreateView.as_view(), name ='TaskCreate'),
    path('delete/<int:pk>/',TaskDeleteView.as_view(), name ='TaskDelete'),
]
