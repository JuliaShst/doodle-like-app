from django.db import models
from django.contrib.auth.models import User

class DateTimeOption(models.Model):
    date_time = models.DateTimeField()
    voter_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)
    

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=60)  # Duration in minutes

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    date_time_options = models.ManyToManyField('DateTimeOption')  

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


