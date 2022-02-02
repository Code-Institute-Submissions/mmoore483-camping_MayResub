from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomAccountManager, Booking, BusinessVariables
from .forms import BookingForm
from datetime import timedelta

class Home(View):
    def get(self, request):
        return render(request, "index.html")


class BookingPage(View):
    def get(self, request):
        return render(request, "booking.html", {'booking_form': BookingForm()})

    def post(self, request, *args, **kwargs):
        available = bool
        if request.method == "POST":
            form = BookingForm(data=request.POST)

            if form.is_valid():
                pitch_type= form.cleaned_data.get("pitch_type")
                date_from = form.cleaned_data.get("date_from")
                date_to = form.cleaned_data.get("date_to")
                queryset = Booking.objects.filter(
                    pitch_type=pitch_type,
                    date_from__range=[date_from,(date_to - timedelta(days=1))]
                    ).exclude(status="cancelled").count()
                BV = BusinessVariables.objects.filter(pitch_type=pitch_type)[:1].values_list("qty", flat=True)

                if queryset < BV[0]:
                    form.save()
                    available = True
                else:
                    available = False
            else:
                return HttpResponseRedirect(reverse('home'))
        return HttpResponseRedirect(reverse('home'))

