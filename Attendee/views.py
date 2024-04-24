from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def list_ateendee(request: HttpRequest) -> HttpResponse:
    return render(request, 'attendee/list_attendee.html') 