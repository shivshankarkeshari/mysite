from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
    path('to_do/', include('todo.urls')),
    path('map/', include('map.urls')),
    path('accounts/', include('accounts.urls')),
    path('metro/', include('metro.urls')),
    path('signups/', include('signups.urls')),
    # path('api/map/', include('map.api_views.loc_list')),
    # path('api/map/', mysite.map.api_views.loc_list),
]
