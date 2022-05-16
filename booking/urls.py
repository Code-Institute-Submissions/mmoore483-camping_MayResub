from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("booking/", views.BookingPage.as_view(), name="booking"),
    path("booking_success/", views.BookingSuccess.as_view(), name="booking_success"),
    path("booking_history/", views.BookingHistory.as_view(), name="booking_history"),

]
