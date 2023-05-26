from django import forms
from .models import Zookeeper

class ZookeeperForm(forms.ModelForm):
    class Meta:
        model = Zookeeper
        fields = '__all__'
