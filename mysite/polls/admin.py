from django.contrib import admin

# Register your models here.
from .models import Engineer
from .models import PresenceInfo

admin.site.register(Engineer)
admin.site.register(PresenceInfo)
