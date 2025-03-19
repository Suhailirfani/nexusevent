from django.db import models

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name = models.CharField(max_length=100)
    cus_phone = models.CharField(max_length=15)
    ev_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date= models.DateField()
    booked_on=models.DateField(auto_now=True)
