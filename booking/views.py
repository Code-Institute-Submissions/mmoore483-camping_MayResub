from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Booking, BusinessVariables, NewUser
from .forms import BookingForm
from datetime import timedelta
from django.contrib import messages


def index(request):
    """Render the home page """
    return render(request, "index.html")


def booking_page(request):
    """Render the booking page """
    if request.method == "GET":
        return render(request, "booking.html", {"booking_form": BookingForm()})
    elif request.method == "POST":
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
                :1].values_list("qty", flat=True)

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


def booking_success(request):
    """Renders the booking success page"""
    return render(request, "booking_success.html")


def booking_history(request):
    """Get bookings for the user currently logged in and render them"""
    customer_id = request.user.customer_id
    bookings = Booking.objects.filter(customer_id=customer_id)
    context = {
        "bookings": bookings,
    }
    return render(request, "booking_history.html", context)


def booking_update(request, pk):
    """Open a specific booking and update it"""
    booking = Booking.objects.get(booking_id=pk)
    form = BookingForm(instance=booking)

    if request.method == "POST":
        form = BookingForm(data=request.POST, instance=booking)
        update_form = form.save(commit=False)
        current_user = request.user.customer_id
        customer_id = NewUser.objects.get(customer_id=current_user)
        update_form.customer_id = customer_id
        update_form.status = "P"

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
                :1].values_list("qty", flat=True)

            if queryset < BV[0]:
                form.save()
                messages.success(request, 'Booking updated.')
                return redirect("booking_history")
            else:
                context = {
                    "unavailable": True,
                    "booking_form": BookingForm()
                }
                return render(request, "booking.html", context)

    context = {
        "booking_form": form
    }
    return render(request, "booking.html", context)


def booking_delete(request, pk):
    """Open a specific booking and delete it"""
    booking = Booking.objects.get(booking_id=pk)
    if request.method == "POST":
        booking.delete()
        messages.error(request, 'Booking Cancelled')
        return redirect("booking_history")
    context = {
        "booking": booking
    }
    return render(request, 'delete_check.html', context)
