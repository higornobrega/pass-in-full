from django.contrib import admin

from .models import CheckIn

# Register your models here.

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdAt')
    