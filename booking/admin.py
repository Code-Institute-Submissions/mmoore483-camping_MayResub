from django.contrib import admin
from .models import Customer, Pitch, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(Pitch)
class CustomerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(Booking)
class CustomerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
