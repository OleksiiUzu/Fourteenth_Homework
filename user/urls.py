from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.user_register, name='user_register'),
    path('history', views.user_history, name='user_history'),
]