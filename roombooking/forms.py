from django import forms
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RoomAvailabilitiesForm(forms.Form):
    start = forms.DateTimeField()
    end = forms.DateTimeField()

    def clean_start(self):
        data = self.cleaned_data['start']

        # Check if a date is not in the past.
        converteddata = data.strftime("%m/%d/%Y %H:%M:%S")
        dateobj = datetime.datetime.strptime(converteddata, "%m/%d/%Y %H:%M:%S")

        if dateobj < datetime.datetime.now():
            print('Error with Start Date')
            raise ValidationError(_('Invalid date - renewal in past'))
        return dateobj

    def clean_end(self):
        data = self.cleaned_data['end']

        # Check if a date is not in the past.
        converteddata = data.strftime("%m/%d/%Y %H:%M:%S")
        dateobj = datetime.datetime.strptime(converteddata, "%m/%d/%Y %H:%M:%S")

        if dateobj < datetime.datetime.now():
            print('Error with End Date')
            raise ValidationError(_('Invalid date - renewal in past'))

        return dateobj