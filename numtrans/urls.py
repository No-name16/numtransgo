from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about/',views.AboutView.as_view() , name='aboutpr'),
    path('instruction/', views.InstrView.as_view(), name='instruction'),
    path('transl/',views.TranslView.as_view() , name='transl'),
    path('translatenum', views.translatenum, name='translatenum')
]