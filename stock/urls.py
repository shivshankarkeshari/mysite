from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='stock_home_page'),
]
