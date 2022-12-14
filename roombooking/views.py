from django.shortcuts import render
from django.views import generic
from .models import Room

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime
from roombooking.forms import RoomAvailabilitiesForm

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def roomavailabilities(request):
    rooms = Room.objects.all
    if request.method == 'POST':
        print("Form is working")
        form = RoomAvailabilitiesForm(request.POST)

        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            print(start)
            print(end)

            

    context = {
        'rooms': rooms,
    }

    
    return render(request, 'roomavailabilities.html', context = context)
    

class RoomListView(generic.ListView):
    model = Room

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