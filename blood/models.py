from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import timedelta, datetime

# Create your models here.

expired = 'expired'
active = 'active'
CHOICES = [(False,expired),(True,active)]


class Blood(models.Model):
    Donor = models.ForeignKey('users.donor', on_delete=models.CASCADE)
    Blood_Group = models.CharField(max_length=2)
    Rh_factor = models.CharField(max_length=1) 
    date_collected = models.DateTimeField(default = timezone.now)
    seeker = models.ForeignKey('users.seeker', models.SET_NULL, blank=True, null=True)
    report = models.FileField(upload_to='reports/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.Donor }'

class Transaction(models.Model):
    Amount = models.PositiveIntegerField()
    Date = models.DateTimeField(default=timezone.now)
    Seeker = models.ForeignKey('users.seeker', models.CASCADE)
    Payment_option = models.CharField(max_length=20)
    Status = models.BooleanField(default = False)

    def __str__(self):
        return f'{ self.Seeker }'


class WB(models.Model):
    blood = models.OneToOneField(Blood, on_delete=models.CASCADE)
    status = models.BooleanField(choices=CHOICES, default=True)
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.blood }'

class PRBC(models.Model):
    blood = models.OneToOneField(Blood, on_delete=models.CASCADE)
    status = models.BooleanField(choices=CHOICES, default=True)
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.blood }'

class FFP(models.Model):
    blood = models.OneToOneField(Blood, on_delete=models.CASCADE)
    status = models.BooleanField(choices=CHOICES, default=True)
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.blood }'

class PC(models.Model):
    blood = models.OneToOneField(Blood, on_delete=models.CASCADE)
    status = models.BooleanField(choices=CHOICES, default=True)
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.blood }'

class CRYO(models.Model):
    blood = models.OneToOneField(Blood, on_delete=models.CASCADE)
    status = models.BooleanField(choices=CHOICES, default=True)
    def __str__(self):
        return f'{ self.id }' + ' ' + f'{ self.blood }'