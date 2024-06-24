from django.contrib import admin
from .models import Student,Admin,Event,Facility,Registration,Booking

# Register your models here.

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Event)
admin.site.register(Facility)
admin.site.register(Registration)
admin.site.register(Booking)