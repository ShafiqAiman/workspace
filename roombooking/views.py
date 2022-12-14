from django.shortcuts import render
from django.views import generic
from .models import Room, Booking

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime
from roombooking.forms import RoomAvailabilitiesForm

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def roomavailabilities(request):
    rooms = Room.objects.all
    bookings = Booking.objects.all
    today = datetime.date.today()
    start = today
    if request.method == 'POST':
        print("The request is POST")
        form = RoomAvailabilitiesForm(request.POST)

        if form.is_valid():
            start = form.cleaned_data['start']
            print(start)
        
    bookings = Booking.objects.filter(startdate = start)

    roomsfilter = Room.objects

    roomlist = []

    for booking in bookings:
        print(booking.room)
        roomlist.append(booking.room)

    rooms = roomsfilter.exclude(name__in = roomlist)
            
            
    context = {
        'rooms': rooms,
        'bookings':bookings,
        'today': today,
        'start': start,
        
    }

    
    return render(request, 'roomavailabilities.html', context = context)
    

class RoomListView(generic.ListView):
    model = Room

class BookingListView(generic.ListView):
    model = Booking

class RoomDetailView(generic.DetailView):
    model = Room

class RoomCreate(CreateView):
    model = Room
    fields = '__all__'

class RoomUpdate(UpdateView):
    model = Room
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('Rooms')