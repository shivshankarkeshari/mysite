from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='stock_home_page'),
    path('feed/', views.background_theme, name='background_template'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
