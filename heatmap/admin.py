from django.contrib import admin
from .models import LatLong

class LatLongAdmin(admin.ModelAdmin):
    model = LatLong
    list_display = ('latitude', 'longitude')

admin.site.register(LatLong, LatLongAdmin)
