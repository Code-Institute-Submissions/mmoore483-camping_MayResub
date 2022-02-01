from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CustomAccountManager, Booking
from .forms import BookingForm


class Home(View):
    def get(self, request):
        return render(request, "index.html")


class Booking(View):
    def get(self, request):
        return render(request, "booking.html", {'booking_form': BookingForm()},)

    def post(self, request):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.pitch_type = request.booking.pitch_type
            booking_form.instance.date_from = request.booking.date_from
            booking_form.instance.date_to = request.booking.date_to
            booking = booking_form.save(commit=False)
            print(booking)
        else:
            booking_form = BookingForm()

        return render(request, "booking.html", {'booking_form': BookingForm()})
