from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import LocationList
from .forms import LocationForm
from django.urls import reverse


def map_view_f(request):
    locations = LocationList.objects.all()
    form = LocationForm()
    context = {'locations': locations, 'form': form}

    if request.method == 'POST':
        print("ok")

        form = LocationForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('map'))

    return render(request, 'map/list.html', context)


def delete_all(request):
    LocationList.objects.all().delete()
    return HttpResponseRedirect(reverse('map'))


def delete_loc(request, pk):
    LocationList.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('map'))


def test(request):
    return render(request, 'map/test.html')
