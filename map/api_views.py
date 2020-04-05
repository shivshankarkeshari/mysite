from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import LocationList
from .serializers import LocationModelSerializer
import time
from django.views.decorators.csrf import csrf_exempt

# for api_view() decorator ___________ loc_list1, loc_list_details1
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins

# for class based api view  _________ loc_list2, loc_list_details2
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework import viewsets

'''
    Authentication
    
     
    Note: If you use BasicAuthentication in production you must ensure that your API is only available over https. You 
    should also ensure that your API clients will always re-request the username and password at login, and will never 
    store those details to persistent storage.
    
    Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.
    
    Session authentication is appropriate for AJAX clients that are running in the same session context as your website.
    
    
    add auth in settings.py
    in installed app add     'rest_framework.authtoken'
    then make migration
    	c56bed0bfadcf2b945b77c3f34fcce872ab2c4f6
    	
    	add in header how authtoken
    	  
    	
    
     
'''


class LocViewSet2(viewsets.ModelViewSet):
    serializer_class = LocationModelSerializer
    queryset = LocationList.objects.all()


# generic view set
class LocViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = LocationModelSerializer
    queryset = LocationList.objects.all()


class LocViewSet1(viewsets.ViewSet):
    # serializer_class = LocationModelSerializer
    # queryset = LocationList.objects.all()

    def list(self, request):
        locations = LocationList.objects.all()
        return Response((LocationModelSerializer(locations, many=True)).data)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = LocationModelSerializer
    queryset = LocationList.objects.all()
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)


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
        print("_" * 15, type(request), '_' * 15);
        time.sleep(5)

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


@api_view(['GET', 'POST'])
def loc_list1(request):
    if request.method == 'GET':

        locations = LocationList.objects.all()
        serializer = LocationModelSerializer(locations, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request type--> <class 'django.core.handlers.wsgi.WSGIRequest'>
        # imp syntax to fetch data
        # data = JSONParser().parse(request)
        data = request.data
        serializer = LocationModelSerializer(data=data)
        print("_" * 15, type(request), '_' * 15);
        time.sleep(5)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def loc_list_details1(request, pk):
    try:
        loc = LocationList.objects.get(pk=pk)
    except LocationList.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # return JsonResponse(LocationModelSerializer(loc).data)
        return Response(LocationModelSerializer(loc).data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        data = request.data
        serializer = LocationModelSerializer(loc, data=data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class LocList2(APIView):

    def get(self, request):
        locations = LocationList.objects.all()
        serializer = LocationModelSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = LocationModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocListDetails2(APIView):

    def get_object(self, pk):
        try:
            return LocationList.objects.get(pk=pk)
        except LocationList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        return Response(LocationModelSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        loc = self.get_object(pk)
        serializer = LocationModelSerializer(loc, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loc = self.get_object(pk)
        loc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
