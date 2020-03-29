from django import forms
from django.forms import ModelForm

from .models import *


class LocationForm(forms.ModelForm):

    class Meta:
        model = LocationList
        fields = '__all__'
