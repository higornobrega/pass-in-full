from django.urls import path

from . import views

app_name = 'attendee'
urlpatterns = [
    path('list_attendee/', views.list_ateendee, name='list_attendee'),

]

