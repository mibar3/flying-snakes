from django.contrib import admin

# Register your models here.
from .models import Passenger, AirlineSeat


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'passenger_age', 'passenger_dob', 'passenger_phone')


admin.site.register(Passenger, PassengerAdmin)


class AirlineSeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'seat_class', 'seat_location')


admin.site.register(AirlineSeat, AirlineSeatAdmin)
