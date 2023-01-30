from django.contrib import admin

# Register your models here.
from .models import AirlineSeat
class AirlineSeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'seat_class', 'seat_location', 'seat_flag','seat_price')


admin.site.register(AirlineSeat, AirlineSeatAdmin)
