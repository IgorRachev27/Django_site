from django import forms
from .models import Order
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
'''
class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'class':'form-control', 'id':'datepicker'}))

class OrderForm2(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'class':'form-control', 'id':'dp'}))
'''

class OrderForm(forms.ModelForm):
    order_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'pho'}))
    coming_date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker'}))
    class Meta:
        model = Order
        fields = ['order_name', 'order_phone', 'coming_date']

    def clean_order_name(self, *args, **kwargs):
        order_name = self.cleaned_data['order_name']
        if (len(order_name) > 20):
            raise ValidationError(_('Поле не должно превышать 20 букв'))
        return order_name

    def clean_order_phone(self, *args, **kwargs):
        order_phone = self.cleaned_data['order_phone']
        if (len(str(order_phone)) != 16):
            raise ValidationError(_('Заполните поле целиком по типу +7(000)000-00-00'))
        if str(order_phone).isalpha():
            raise ValidationError(_('В номере могут быть только цифры'))
        return order_phone



class OrderForm2(forms.ModelForm):
    order_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}),help_text='не более 20 символов')
    order_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'ph'}),help_text='формат номера 9991234567, 10 цифр')
    coming_date = forms.DateField(label='Date',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'dp'}),help_text='Формат даты, либо воспользуйтесь календарем')

    class Meta:
        model = Order
        fields = ['order_name', 'order_phone', 'coming_date']

    def clean_order_name(self, *args, **kwargs):
        order_name = self.cleaned_data['order_name']
        if (len(order_name) > 20):
            raise ValidationError(_('Поле не должно превышать 20 букв'))
        return order_name

    def clean_order_phone(self, *args, **kwargs):
        order_phone = self.cleaned_data['order_phone']
        if (len(str(order_phone)) != 16):
            raise ValidationError(_('Заполните поле целиком по типу +7(000)000-00-00'))
        if str(order_phone).isalpha():
            raise ValidationError(_('В номере могут быть только цифры'))
        return order_phone