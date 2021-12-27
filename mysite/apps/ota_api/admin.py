from django.contrib import admin
from .models import Firmware, Device

admin.site.register(Firmware)
admin.site.register(Device)