from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(TimePlace)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(Order)
