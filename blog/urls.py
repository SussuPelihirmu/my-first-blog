# importing django's function path and views from application
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]