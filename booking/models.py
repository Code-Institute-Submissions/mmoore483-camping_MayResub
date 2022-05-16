from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class BusinessVariables(models.Model):
    """Business Variable table to set up the types of pitches and quantities """

    pitch_type = models.CharField(max_length=10)
    qty = models.SmallIntegerField(default=20)

    def __str__(self):
        return self.pitch_type


class CustomAccountManager(BaseUserManager):
    """Creation of users both superusers and customers """

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    customer_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    """Booking table to hold reservation details and be queried in views """
    PENDING = "P"
    CANCELLED = "C"
    APPROVED = "A"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CANCELLED, "Cancelled"),
        (APPROVED, "Approved"),
    ]
    booking_id = models.AutoField(primary_key=True, unique=True)
    customer_id = models.ForeignKey(
        NewUser, on_delete=models.PROTECT
    )
    pitch_type = models.ForeignKey(
        BusinessVariables, on_delete=models.PROTECT, default=""
    )
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)

    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default="P")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
