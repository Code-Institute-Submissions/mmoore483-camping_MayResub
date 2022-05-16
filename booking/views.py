from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomAccountManager, Booking, BusinessVariables, NewUser
from .forms import BookingForm
from datetime import timedelta


class Home(View):
    """Render the home page """
    def get(self, request):
        return render(request, "index.html")


class BookingPage(View):
    def get(self, request):
        """Render the booking page """
        return render(request, "booking.html", {"booking_form": BookingForm()})


# Receive post data, filter the booking database and compare the number of bookings
# in that date range to the number of pitches set in business variable. if available,
# save the booking and return to the home page. If not, return to the home page

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = BookingForm(data=request.POST)
            update_form = form.save(commit=False)
            current_user = request.user.customer_id
            customer_id = NewUser.objects.get(customer_id=current_user)
            update_form.customer_id = customer_id
            unavailable = False
            if form.is_valid():
                pitch_type = form.cleaned_data.get("pitch_type")
                date_from = form.cleaned_data.get("date_from")
                date_to = form.cleaned_data.get("date_to")
                queryset = (Booking.objects.filter(
                    pitch_type=pitch_type,
                    date_from__range=[date_from,
                                      (date_to - timedelta(days=1))],
                )
                    .exclude(status="cancelled")
                    .count()
                )
                BV = BusinessVariables.objects.filter(pitch_type=pitch_type)[
                    :1
                ].values_list("qty", flat=True)

                if queryset < BV[0]:
                    form.save()
                    return HttpResponseRedirect(reverse("booking_success"))
                else:
                    context = {
                        "unavailable": True,
                        "booking_form": BookingForm()
                    }
                    return render(request, "booking.html", context)

            else:
                return HttpResponseRedirect(reverse("home"))


class BookingSuccess(View):
    def get(self, request):
        return render(request, "booking_success.html")


class BookingHistory(View):
    def get(self, request):
        bookings = Booking.objects.filter(customer_id=self.request.user.customer_id)
        context = {
            "bookings": bookings,
        }
        return render(request, "booking_history.html", context)


class BookingDetail(View):
    def post(self, request, *args, **kwargs):

        return render(request, "booking_detail.html", context)
