from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def list_attendee(request: HttpRequest) -> HttpResponse:
    return render(request, 'attendee/list_attendee.html') 

def create_attendee(request: HttpRequest) -> HttpResponse:
    return render(request, 'attendee/create_attendee.html')

def update_attendee(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'attendee/update_attendee.html')