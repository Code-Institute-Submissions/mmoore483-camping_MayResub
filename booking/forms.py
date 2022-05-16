from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    """ Simple form for customer reservation request"""
    class Meta:
        model = Booking
        fields = ("pitch_type", "date_from", "date_to")
