from django import forms
from .models import Zone

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = '__all__'
