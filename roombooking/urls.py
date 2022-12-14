from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('rooms/availabilities/', views.roomavailabilities, name='rooms-availabilities'),
    path('room/<int:pk>', views.RoomDetailView.as_view(), name='room-detail'),
    path('room/create/', views.RoomCreate.as_view(), name='room-create'),
    path('room/<int:pk>/update/', views.RoomUpdate.as_view(), name='room-update'),
    path('room/<int:pk>/delete/', views.RoomDelete.as_view(), name='room-delete'),
]