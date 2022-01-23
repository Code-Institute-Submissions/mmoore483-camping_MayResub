from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser, Booking, BusinessVariables

admin.site.site_header = "Heatherhope Campsite Administration"

# Register your models here.


@admin.register(BusinessVariables)
class BusinessVariableAdmin(admin.ModelAdmin):
    list_display = ("pitch_type", "qty")
    list_editable = ("qty",)
    # search_fields = ("pitch_type",)


@admin.register(NewUser)
class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('-first_name',)
    list_display = ("email", 'first_name', 'last_name', "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", 'first_name', 'last_name', "phone")}),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("booking_id", "status", "created_on", "pitch_type", "date_to", "date_from")
    list_editable = ("status", )
