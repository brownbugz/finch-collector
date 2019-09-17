from django.contrib import admin
from .models import Planner, Accessory, Gadget

# Register your models here.

admin.site.register(Planner)
admin.site.register(Accessory)
admin.site.register(Gadget)
admin.site.register(Photo)