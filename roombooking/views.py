from django.shortcuts import render
from django.views import generic
from .models import Room, Booking

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.admin.widgets import AdminDateWidget, AdminRadioSelect
from django.shortcuts import HttpResponse, HttpResponseRedirect

import datetime
from roombooking.forms import BookingForm

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def roomavailabilities(request):
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    today = datetime.date.today()
    start = today
    if request.method == 'POST':
        start = request.POST["start"]
        
    bookings = Booking.objects.filter(startdate = start)
            
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

class BookingCreate(FormView):
    model = Booking
    form_class = BookingForm
    template_name = 'roombooking/create_booking.html'
    initial = {'startdate': datetime.date.today(), 'enddate': datetime.date.today()}

    def form_valid(self, form):
        data = form.cleaned_data
        print(check_availability(data))
        if check_availability(data):
            booking = Booking.objects.create(
                startdate = data['startdate'],
                enddate = data['enddate'],
                starttime = data['starttime'],
                endtime = data['endtime'],
                room = data['room'],
                organizer = self.request.user
            )
            booking.save()
            return HttpResponseRedirect(reverse('bookings'))
        else:
            return HttpResponse("The slot is unavailable!")

def check_availability(data):
        bookings = Booking.objects.filter(room = data['room'], startdate = data['startdate'])

        availabilitylist = []
        
        if bookings:
            for booking in bookings:
            
                if (data['endtime'].time <= booking.starttime.time or data['starttime'].time > booking.endtime.time):
                    availabilitylist.append(True)
                else:
                    return False
        else:
            return True
        
        return all(availabilitylist)
    
class BookingUpdate(UpdateView):
    model = Booking
    fields = '__all__' # Not recommended (potential security issue if more fields added)

    def get_form(self, form_class=None):
        form = super(BookingUpdate, self).get_form(form_class)
        form.fields['startdate'].widget = AdminDateWidget(attrs={'type': 'date'})
        
        form.fields['enddate'].widget = AdminDateWidget(attrs={'type': 'date'})
        
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