from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import donor, seeker

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class DonorRegisterForm(forms.ModelForm):
    class Meta:
        model = donor
        fields = ['age', 'gender', 'Blood_Group', 'Rh_factor', 'contact_number', 'address','city', 'show']


class SeekerRegisterForm(forms.ModelForm):
    class Meta:
        model = seeker
        fields = ['first_name', 'last_name', 'age', 'gender', 'Blood_Group', 'Rh_factor', 'contact_number', 'address', 'city', 'hospital_name', 'hospital_address', 'blood_quantity']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class DonorUpdateForm(forms.ModelForm):
    class Meta:
        model = donor
        fields = ['contact_number', 'address', 'city', 'show']