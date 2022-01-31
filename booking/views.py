from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CustomAccountManager
from .forms import BookingForm


class Home(View):
    def get(self, request):
        return render(request, "index.html")

class Booking(View):
    def get(self, request):
        return render(request, "booking.html", {'booking_form': BookingForm()},)

