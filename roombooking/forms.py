from django import forms
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RoomAvailabilitiesForm(forms.Form):
    start = forms.DateField()

    def clean_start(self):
        data = self.cleaned_data['start']

        if data < datetime.date.today():
            print('Error with Start Date')
            raise ValidationError(_('Invalid date - renewal in past'))
        return data
