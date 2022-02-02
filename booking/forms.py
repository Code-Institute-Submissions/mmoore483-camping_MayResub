from .models import Booking
from django import forms

""" Simple form for customer reservation request"""
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("pitch_type", "date_from", "date_to")
