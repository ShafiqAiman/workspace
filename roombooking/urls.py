from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('bookings/', views.BookingListView.as_view(), name='bookings'),
    path('rooms/availabilities/', views.roomavailabilities, name='rooms-availabilities'),
    path('room/<int:pk>', views.RoomDetailView.as_view(), name='room-detail'),
    path('booking/<int:pk>', views.BookingDetailView.as_view(), name='booking-detail'),
    path('room/create/', views.RoomCreate.as_view(), name='room-create'),
    path('room/<int:pk>/update/', views.RoomUpdate.as_view(), name='room-update'),
    path('room/<int:pk>/delete/', views.RoomDelete.as_view(), name='room-delete'),
    path('booking/create/', views.BookingCreate.as_view(), name='booking-create'),
    path('booking/<int:pk>/update/', views.BookingUpdate.as_view(), name='booking-update'),
    path('booking/<int:pk>/delete/', views.BookingDelete.as_view(), name='booking-delete'),
]