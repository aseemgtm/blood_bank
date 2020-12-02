from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

GENDER_MALE = 'M'
GENDER_FEMALE = 'F'
GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),]

BLOOD_A = 'A'
BLOOD_B = 'B'
BLOOD_AB = 'AB'
BLOOD_O = 'O'
BLOOD_CHOICES = [(BLOOD_A, 'A'), (BLOOD_B, 'B'), (BLOOD_AB, 'AB'), (BLOOD_O, 'O'),]

Rh_positive = '+'
Rh_negative = '-'
Rh_CHOICES = [(Rh_positive, '+'), (Rh_negative, '-'),]

yes = 'Yes'
no = 'No'
SHOW_CHOICES = [(yes, 'Yes'), (no, 'No')]

PRBC='PRBC'
WB='WB'
FFP='FFP'
PC='PC'
CRYO='CRYO'
TYPE_CHOICE = [(PRBC,'PRBC'),(WB,'WB'),(FFP,'FFP'),(PC,'PC'),(CRYO,'CRYO')]

class donor( models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    Blood_Group = models.CharField(choices=BLOOD_CHOICES, max_length=2)
    Rh_factor = models.CharField(choices=Rh_CHOICES, max_length=1) 
    contact_number = models.BigIntegerField()
    address = models.CharField(max_length=100, help_text='eg : #112 Sector 40C', default=' ')
    show = models.CharField(verbose_name='Can we make your contact details public for people in need to contact you?', choices=SHOW_CHOICES, default='Yes', max_length=3)
    city = models.CharField(max_length=50, default=' ')

    def __str__(self):
        return f'{ self.user.username }'

class seeker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    Blood_Group = models.CharField(choices=BLOOD_CHOICES, max_length=2)
    Rh_factor = models.CharField(choices=Rh_CHOICES, max_length=1) 
    date_registered = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=100, help_text='eg : #112 Sector 40C', default=' ')
    contact_number = models.BigIntegerField()
    hospital_name = models.CharField(max_length=100, default=' ', help_text='eg: GMSH')
    hospital_address = models.CharField(max_length=100, help_text='eg: sector 16, Chandigarh', default=' ')
    blood_quantity = models.IntegerField(default=0)
    blood_type = models.CharField(max_length=4, choices=TYPE_CHOICE, default=' ')
    city = models.CharField(max_length=50, default=' ')

    def __str__(self):
        return f'{ self.first_name }' + ' ' + f'{ self.last_name }'