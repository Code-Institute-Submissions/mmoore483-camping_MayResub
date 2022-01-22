from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    email = models.EmailField()

class Pitch(models.Model):
    TENT = 'T'
    VAN = 'V'
    CARAVAN = 'C'
    MOTORHOME = 'M'
    PITCH_TYPE_CHOICES = [
        (TENT, 'Tent'),
        (VAN, 'Van'),
        (CARAVAN, 'Caravan'),
        (MOTORHOME, 'Motorhome'),
    ]
    pitch_id = models.AutoField(primary_key=True, unique=True)
    pitch_type = models.CharField(max_length=2, choices=PITCH_TYPE_CHOICES)
    availability = models.BooleanField(default=True)
    date = models.DateField()

class Booking(models.Model):
    PENDING = 'P'
    CANCELLED = 'C'
    APPROVED = 'A'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CANCELLED, 'Cancelled'),
        (APPROVED, 'Approved'),
    ]
    booking_id = models.AutoField(primary_key=True, unique=True)
    pitch_want = models.CharField(max_length=2, choices=Pitch.PITCH_TYPE_CHOICES)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pitch_id = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
