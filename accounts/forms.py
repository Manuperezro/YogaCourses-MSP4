from django import forms
from .models import Student


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['avatar', 'default_phone_number', 'default_postcode', 'default_town_or_city', 'default_street_address1', 'default_street_address2', 'default_county']
