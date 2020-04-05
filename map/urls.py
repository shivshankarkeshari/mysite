from django.urls import path, include
from . import views, api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', api_views.LocViewSet, basename='asd')


urlpatterns = [
    path('', views.map_view_f, name="map"),
    path('delete/<str:pk>/', views.delete_loc, name="delete location"),
    path('delete_all/', views.delete_all, name="delete all location"),
    path('2/', views.test, name="test"),
    path('api/g/loc_list/<int:pk>/', api_views.GenericAPIView.as_view(), name="map-api"),
    path('api/loc_list/', api_views.loc_list, name="map-api"),
    path('api/loc_list/<int:pk>/', api_views.loc_list_details, name="map-api-details"),
    path('api/loc_list1/', api_views.loc_list1, name="fmap-api"),
    path('api/loc_list1/<int:pk>/', api_views.loc_list_details1, name="fmap-api-details"),
    path('api/loc_list2/', api_views.LocList2.as_view(), name="cmap-api"),
    path('api/loc_list2/<int:pk>/', api_views.LocListDetails2.as_view(), name="cmap-api-details"),
    path('viewset/', api_views.LocViewSet),
    path('api/', include(router.urls)),
]


