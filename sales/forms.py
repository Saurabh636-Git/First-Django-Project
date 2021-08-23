from django import forms
from django.db.models import fields
from django.forms import ModelForm, models, widgets
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'



class NumberInput(forms.NumberInput):
    input_type = 'total'

class NumberInput(forms.NumberInput):
    input_type = 'quantity'


class SalesForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['items','quantity','date']
        widgets = {
            'items': forms.Select(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'total': NumberInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
        }

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'