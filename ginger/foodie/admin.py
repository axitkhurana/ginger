from django.contrib import admin

from ginger.foodie.models import Vendor, Event


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_time')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Event, EventAdmin)
