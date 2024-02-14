from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
