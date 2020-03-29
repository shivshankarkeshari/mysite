from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view_f, name="map"),
    path('delete/<str:pk>/', views.delete_loc, name="delete location"),
    path('delete_all/', views.delete_all, name="delete all location"),
    path('2/', views.test, name="test"),
]


