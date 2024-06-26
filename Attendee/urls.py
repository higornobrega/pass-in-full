from django.urls import path

from . import views

app_name = 'attendee'
urlpatterns = [
    path('list_attendee/', views.list_attendee, name='list_attendee'),
    path('create_attendee/', views.create_attendee, name='create_attendee'),
    path('update_attendee/<int:pk>/', views.update_attendee, name='update_attendee'),
    path('delete_attendee/<int:pk>/', views.delete_attendee, name='delete_attendee')
]

