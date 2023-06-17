from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
import uuid 

class Room(models.Model):
    name = models.CharField(max_length=255)
    room_pic = models.ImageField(upload_to="images/", null=True)
    dateadded = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('room-update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('room-delete', args=[str(self.id)])

    def get_picture_url(self):
        if self.room_pic:
            return 'http://127.0.0.1:8000/' + self.room_pic.url
        return ''

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class StartTime(models.Model):
    time =  models.TimeField()

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.time)

class EndTime(models.Model):
    time =  models.TimeField()

    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.time)

class Booking(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this booking")
    startdate = models.DateField()
    starttime = models.ForeignKey(StartTime, on_delete=models.PROTECT, null=True)
    enddate = models.DateField()
    endtime = models.ForeignKey(EndTime, on_delete=models.PROTECT, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    dateadded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dateadded']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.startdate, self.room.name)

    def get_absolute_url(self):
        return reverse('booking-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('booking-update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('booking-delete', args=[str(self.id)])


    