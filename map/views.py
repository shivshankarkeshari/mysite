from django.http import HttpResponseRedirect

from django.shortcuts import render
from .models import LocationList
from .forms import LocationForm
from django.urls import reverse
from math import radians, cos, sin, asin, sqrt
from . import tests


def map_view_f(request):
    locations = LocationList.objects.all()
    form = LocationForm()

    if len(locations):
        a = []
        for j in range(len(locations)):
            a.append([])
            for i in range(len(locations)):
                a[j].append(
                    distance(float(locations[j].latitude), float(locations[i].latitude), float(locations[j].longitude),
                             float(locations[i].longitude)))
        v = tests.main(a)
    else:
        v = "Ok"

    context = {'locations': locations, 'form': form, 'v': v}

    if request.method == 'POST':
        form = LocationForm(request.POST)
        # print(len(request.POST['latitude']))
        print(request.POST)

        if form.is_valid() and (len(request.POST['latitude']) != 0 and len(request.POST['latitude']) != 0):
            form.save()
            return HttpResponseRedirect(reverse('map'))

    return render(request, 'map/list.html', context)


def delete_all(request):
    LocationList.objects.all().delete()
    return HttpResponseRedirect(reverse('map'))


def delete_loc(request, pk):
    LocationList.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('map'))


def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))
    r = 6371
    return c*r


def test(request):

    if request.method == 'POST':
        form = LocationForm(request.POST)

        if form.is_valid() and (len(request.POST['latitude']) != 0 and len(request.POST['latitude']) != 0):
            form.save()
            locations = LocationList.objects.all()
            return render(request, 'map/locations_list.html', {'locations': locations})
