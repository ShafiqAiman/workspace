from django.contrib import admin
from .models import Room, Booking, StartTime, EndTime

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(StartTime)
admin.site.register(EndTime)