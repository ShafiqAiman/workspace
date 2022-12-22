from django import forms

from .models import Room, StartTime, EndTime, Booking
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
        room = cleaned_data.get("room")
        print(type(starttime.time))
        
        if startdate < datetime.date.today() or enddate < datetime.date.today():
            print('Error with Date')
            raise ValidationError(_('Invalid Date - Date is in past'))

        if starttime.time >  endtime.time:
            print('Error with Time')
            raise ValidationError(_('Invalid Time - Start Time cannot be after End Time'))

        if check_availability(room, startdate, endtime, starttime):
            return cleaned_data
        else:
            raise ValidationError(_('The slot is unavailable!'))

def check_availability(room, startdate, endtime, starttime):
        bookings = Booking.objects.filter(room = room, startdate = startdate)
        

        availabilitylist = []
        
        if bookings:
            for booking in bookings:
                
                if (endtime.time <= booking.starttime.time or starttime.time >= booking.endtime.time):
                    availabilitylist.append(True)
                else:
                    return False
        else:
            return True
        
        return all(availabilitylist)
        
