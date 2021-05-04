from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meeting(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingId=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return str(self.meetingId)
    
    class Meta:
        db_table='meetingMinutes'
        verbose_name_plural='minutes'

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    resourceURL=models.URLField()
    userId=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userId=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventTitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'
