from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
import uuid 

class Room(models.Model):
    name = models.CharField(max_length=255)
    dateadded = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('room-update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('room-delete', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Booking(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this booking")
    startdate = models.DateField()
    starttime = models.TimeField(default=datetime.datetime.now())
    enddate = models.DateField()
    endtime = models.TimeField(default=datetime.datetime.now())
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    dateadded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.startdate, self.room.name)

    def get_absolute_url(self):
        return reverse('booking-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('booking-update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('booking-delete', args=[str(self.id)])

# class Time(models.Model):
#     Options = (
#         ("08:00 AM", "08:00 AM"),
#         ("09:00 AM", "09:00 AM"),
#         ("10:00 AM", "10:00 AM"),
#         ("11:00 AM", "11:00 AM"),
#         ("12:00 PM", "12:00 PM"),
#         ("01:00 PM", "01:00 PM"),
#         ("02:00 PM", "02:00 PM")
#     )

#     time =  models.TimeField(
#         choices=Options
#     )
    