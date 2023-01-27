from django.db import models
from django.urls import reverse


class Passenger(models.Model):
    passenger_name = models.CharField(max_length=50, help_text="Enter your name")
    passenger_age = models.IntegerField(help_text="Enter your age")
    passenger_phone = models.IntegerField(help_text="Enter your phone number")
    passenger_dob = models.DateField()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.passenger_name


class AirlineSeat(models.Model):
    """A typical class defining a model, derived from the Model class."""

    class SeatType(models.TextChoices):
        FIRST = "1", "FIRST"
        BUSINESS = "2", "BUSINESS"
        ECONOMY = "3", "ECONOMY"
        EMERGENCY = '4', 'EMERGENCY'

    class SeatLocation(models.TextChoices):
        WINDOW = '1', 'Window seat'
        MIDDLE = '2', 'Middle seat'
        AISLE = '3', 'Aisle seat'

    class SeatFlags(models.TextChoices):
        RED = '1', 'TAKEN'
        GREEN = '2', 'SELECTED'
        GREY = '3', 'AVAILABLE'

    ''' class SeatRow(models.TextChoices):
        ONE = '1'
        TWO = '2'
        THREE = '3'
        FOUR = '4'
        FIVE = '5'
        SIX = '6'
        SEVEN = '7'
        EIGHT = '8'
        NINE = '9'
        TEN  = '10' '''

    # Fields
    seat_number = models.CharField(max_length=20, help_text='Enter seat number')
    seat_class = models.CharField(
        max_length=10,
        choices=SeatType.choices,
        default=SeatType.ECONOMY
    )
    seat_location = models.CharField(
        max_length=20,
        choices=SeatLocation.choices,
        default=SeatLocation.AISLE
    )

    seat_flag = models.CharField(
        max_length=15,
        choices=SeatFlags.choices,
        default=SeatFlags.GREY)

    ''' seat_row = models.CharField(
        max_length=5,
        choices=SeatRow.choices,
        default=SeatRow.ONE) '''


    # Metadata
    class Meta:
        ordering = ['-seat_number', 'seat_class', 'seat_location', 'seat_flag']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.seat_number
