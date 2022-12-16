from django.shortcuts import render
from django.views import generic
from .models import Room, Booking

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.widgets import AdminDateWidget, AdminRadioSelect

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
            print("Valid date")
        
    bookings = Booking.objects.filter(startdate = start)

    # roomsfilter = Room.objects

    roomlist = []
    # timelist = []
    

    for booking in bookings:
        roomlist.append(booking.room)
        # timelist.append([booking.starttime, booking.endtime])
        print(roomlist)
    #     print(timelist)


    # rooms = roomsfilter.exclude(name__in = roomlist)
            
            
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

class BookingDetailView(generic.DetailView):
    model = Booking

class RoomCreate(CreateView):
    model = Room
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super(RoomCreate, self).get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control'})
        return form

class RoomUpdate(UpdateView):
    model = Room
    fields = '__all__' # Not recommended (potential security issue if more fields added)

    def get_form(self, form_class=None):
        form = super(RoomUpdate, self).get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control'})
        return form

class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('Rooms')

class BookingCreate(CreateView):
    model = Booking
    fields = ['startdate','starttime', 'enddate', 'endtime','room', 'organizer']
    initial = {'startdate': datetime.date.today(), 'enddate': datetime.date.today()}

    def get_form(self, form_class=None):
        form = super(BookingCreate, self).get_form(form_class)
        form.fields['startdate'].widget = AdminDateWidget(attrs={'type': 'date'})
        # form.fields['starttime'].widget = AdminDateWidget(attrs={'type': 'time'})
        form.fields['enddate'].widget = AdminDateWidget(attrs={'type': 'date'})
        # form.fields['endtime'].widget = AdminDateWidget(attrs={'type': 'time'})
        form.fields['startdate'].widget.attrs.update({'class': 'form-control'})
        form.fields['starttime'].widget.attrs.update({'class': 'form-control'})
        form.fields['enddate'].widget.attrs.update({'class': 'form-control'})
        form.fields['endtime'].widget.attrs.update({'class': 'form-control'})
        form.fields['room'].widget.attrs.update({'class': 'form-control'})
        form.fields['organizer'].widget.attrs.update({'class': 'form-control'})
        return form

class BookingUpdate(UpdateView):
    model = Booking
    fields = '__all__' # Not recommended (potential security issue if more fields added)

    def get_form(self, form_class=None):
        form = super(BookingUpdate, self).get_form(form_class)
        form.fields['startdate'].widget = AdminDateWidget(attrs={'type': 'date'})
        # form.fields['starttime'].widget = AdminDateWidget(attrs={'type': 'time'})
        form.fields['enddate'].widget = AdminDateWidget(attrs={'type': 'date'})
        # form.fields['endtime'].widget = AdminDateWidget(attrs={'type': 'time'})
        form.fields['startdate'].widget.attrs.update({'class': 'form-control'})
        form.fields['starttime'].widget.attrs.update({'class': 'form-control'})
        form.fields['enddate'].widget.attrs.update({'class': 'form-control'})
        form.fields['endtime'].widget.attrs.update({'class': 'form-control'})
        form.fields['room'].widget.attrs.update({'class': 'form-control'})
        form.fields['organizer'].widget.attrs.update({'class': 'form-control'})
        return form

class BookingDelete(DeleteView):
    model = Booking
    success_url = reverse_lazy('Bookings')