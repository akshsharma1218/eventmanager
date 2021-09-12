from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('liked_event/', views.liked_event, name="liked_event"),
    path('like_event/', views.like_event, name="like_event"),
    path('search/', views.SearchResultView.as_view(), name='search-result'),
    path('event/',views.EventCreateView.as_view(),name="event_create")
]
