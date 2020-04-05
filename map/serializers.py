from rest_framework import serializers
from .models import LocationList
from rest_framework.renderers import JSONRenderer

'''
-->using element of model class
>>> a.__dict__
{'_state': <django.db.models.base.ModelState object at 0x7f55bd6b81d0>, 'id': 242, 'name': '-', 'latitude': Decimal('25.0400000000000000'), 'longitude': Decimal('79.7100000000000000')}

-->using dict 
>>> a
{'name': 'shiv', 'latitude': 12, 'longitude': 12}
>>> s = LocationListSerializer(a)
>>> s.data
{'name': 'shiv', 'latitude': '12.0000000000000000', 'longitude': '12.0000000000000000'}
>>> JSONRenderer().render(s.data)
b'{"name":"shiv","latitude":"12.0000000000000000","longitude":"12.0000000000000000"}'

--> for serializing queryset data many
>>> a = LocationList.objects.all()
>>> s = LocationListSerializer(a, many=True)

'''
from rest_framework.parsers import JSONParser

'''
    when define serializer.Serializer we need to specify all 
    of our fields that we have, also we can use Form or ModelForm class 
    
    Django have 2 types of form 
    > form class (we need to specify all fields)
    > model form class (don't need to specify all fields)
    
'''


# manual serializer
class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    latitude = serializers.DecimalField(max_digits=22, decimal_places=16)
    longitude = serializers.DecimalField(max_digits=22, decimal_places=16)

    def create(self, validated_data):
        return LocationList.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance


# model serializer
# >>> print(repr(LocationModelSerializer()))
class LocationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationList
        fields = '__all__'

        # fields = ['name', 'latitude' ]


# function based api views
# generic based views

