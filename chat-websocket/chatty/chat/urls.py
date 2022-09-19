from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('<str:room_name>/',views.RoomView,name='room'),
]
