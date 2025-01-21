from django.contrib import admin
from .models import CustomUser, Destination, Booking, Tourist, Tour, TourDay

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Destination)

admin.site.register(Tourist)
admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(TourDay)