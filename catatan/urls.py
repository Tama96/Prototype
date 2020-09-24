
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
]
    # path('<id>/update/', views.update),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)