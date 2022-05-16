from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("booking/", views.booking_page, name="booking"),
    path("booking_success/", views.booking_success, name="booking_success"),
    path("booking_history/", views.booking_history, name="booking_history"),
    path("booking_update/<str:pk>", views.booking_update, name="booking_update"),
]
