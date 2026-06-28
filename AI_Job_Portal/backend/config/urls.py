"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home),

    path('login/', views.login),

    path('logout/', views.logout),

    path('register/', views.register),

    path('jobs/', views.jobs),

    path('apply/<int:job_id>/', views.apply_job),

    path('about/', views.about),

    path('contact/', views.contact),

    path('my-applications/', views.my_applications),

    path('dashboard/', views.dashboard),

    path("recommendation/", views.recommendation),

]