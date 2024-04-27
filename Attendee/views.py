from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Attendee


def create_attendee(request: HttpRequest) -> HttpResponse:
    return render(request, 'attendee/create_attendee.html')

def list_attendee(request: HttpRequest) -> HttpResponse:
    attendees = Attendee.objects.all().order_by('name')
    context = {
        'attendees':attendees,
    }
    return render(request, 'attendee/list_attendee.html', context) 

def update_attendee(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'attendee/update_attendee.html')

def delete_attendee(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'attendee/list_attendee.html')