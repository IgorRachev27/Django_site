from django import forms
from .models import Order

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'class':'form-control', 'id':'datepicker'}))

class OrderForm2(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'class':'form-control', 'id':'dp'}))
