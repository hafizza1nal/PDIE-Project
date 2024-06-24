from django.db import models

class Student(models.Model):
    Studentid = models.AutoField(primary_key=True)
    Studentpass = models.TextField(max_length=20)
    Studentname = models.CharField(max_length=30)

    def __str__(self):
        return self.Studentname

class Admin(models.Model):
    Adminid = models.CharField(max_length=10, primary_key=True)
    Adminpass = models.TextField(max_length=20)

class Event(models.Model):
    Eventname = models.CharField(max_length=255, primary_key=True)
    Eventdescription = models.CharField(max_length=100)
    EventDate = models.DateField()

    def __str__(self):
        return self.Eventname

class Facility(models.Model):
    Facilityname = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.Facilityname

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.Studentname} registered for {self.event.Eventname}'
    

class Booking(models.Model):
    bookingid = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.Studentname} booked for {self.facility.Facilityname}'