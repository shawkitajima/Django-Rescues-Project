from django.contrib import admin
from .models import Rescue, Gift, Adopter

# Register your models here.

admin.site.register(Rescue)
admin.site.register(Gift)
admin.site.register(Adopter)