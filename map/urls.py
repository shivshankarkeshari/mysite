from django.urls import path
from . import views, api_views


urlpatterns = [
    path('', views.map_view_f, name="map"),
    path('delete/<str:pk>/', views.delete_loc, name="delete location"),
    path('delete_all/', views.delete_all, name="delete all location"),
    path('2/', views.test, name="test"),
    path('api/loc_list/', api_views.loc_list, name="map-api"),
    path('api/loc_list/<int:pk>/', api_views.loc_list_details, name="map-api-details"),
]


