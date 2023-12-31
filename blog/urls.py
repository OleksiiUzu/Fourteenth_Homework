from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.blog_post, name='blog_post'),
    path('feedback', views.feedback, name='feedback')
]
