from django.contrib import admin

# Register your models here.

from .models import Station, Users, TrainData, UserTravelDetails

admin.site.register([Station, Users, TrainData, UserTravelDetails])
