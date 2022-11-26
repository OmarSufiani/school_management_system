from django import forms
from django.forms import ModelForm
from .models import *

#create forms here
class Markform(ModelForm):
    class Meta:
        model=Mark
        fields="__all__"