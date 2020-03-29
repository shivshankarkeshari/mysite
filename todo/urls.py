from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_f, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('del/', views.delete_all, name="delete all"),
]

