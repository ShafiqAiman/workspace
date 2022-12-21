from django import forms

from .models import Room, StartTime, EndTime
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class BookingForm(forms.Form):
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    enddate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    starttime = forms.ModelChoiceField(queryset=StartTime.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    endtime = forms.ModelChoiceField(queryset=EndTime.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    room = forms.ModelChoiceField(queryset=Room.objects.all(), widget= forms.Select(attrs={'class': 'form-control'}))
   
    def clean(self):
        cleaned_data = super().clean()
        startdate = cleaned_data.get("startdate")
        enddate = cleaned_data.get("enddate")
        starttime = cleaned_data.get("starttime")
        endtime = cleaned_data.get("endtime")
        print(type(starttime.time))
        
        if startdate < datetime.date.today() or enddate < datetime.date.today():
            print('Error with Date')
            raise ValidationError(_('Invalid date - date is in past'))

        if starttime.time >  endtime.time:
            print('Error with Time')
            raise ValidationError(_('Invalid time - time is in past'))

        return cleaned_data


        
