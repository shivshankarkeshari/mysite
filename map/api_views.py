from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import LocationList
from .serializers import LocationModelSerializer
import time
from django.views.decorators.csrf import csrf_exempt

'''
https://www.youtube.com/watch?v=B38aDwUpcFc

learn:
    Django REST Framework  Serializer
    REST Framework Modal Serializer
    REST Framework Function Based API Views
    REST Framework api_view() Decorator 
    REST Class Based API Views
    REST Generic Views & Mixins
    REST Framework Authentication
    REST Framework Viewsets & Routers
    REST Framework Generic Viewsets
    REST Framework Modal Viewsets 
    

Note:
    that because we want to be able to POST to this view from clients that won't have a CSRF token we need to 
    mark the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views actually 
    use more sensible behavior than this, but it'll do for our purposes right now. 
'''


@csrf_exempt
def loc_list(request):
    if request.method == 'GET':

        locations = LocationList.objects.all()
        serializer = LocationModelSerializer(locations, many=True)
        '''
        print(type(serializer), type(serializer.data))
        <class 'rest_framework.serializers.ListSerializer'> <class 'rest_framework.utils.serializer_helpers.ReturnList'>
        In your view instead of using Response(serializer) you need to use Response(serializer.data)
        '''
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # request type--> <class 'django.core.handlers.wsgi.WSGIRequest'>
        # imp syntax to fetch data
        data = JSONParser().parse(request)
        serializer = LocationModelSerializer(data=data)
        print("_"*15, type(request), '_'*15); time.sleep(5)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


def loc_list_details(request, pk):
    try:
        loc = LocationList.objects.get(pk=pk)
    except LocationList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(LocationModelSerializer(loc).data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocationModelSerializer(loc, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        loc.delete()
        return HttpResponse(status=204)
