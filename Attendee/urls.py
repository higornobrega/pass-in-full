from django.urls import path

from . import views

app_name = 'attendee'
urlpatterns = [
    path('list_attendee/', views.list_attendee, name='list_attendee'),
    path('create_attendee/', views.create_attendee, name='create_attendee'),
]

