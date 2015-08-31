from django import forms
from django.forms import ModelForm
from testapp.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_id','client_id','timestamp']