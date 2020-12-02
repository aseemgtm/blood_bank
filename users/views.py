from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, DonorRegisterForm, DonorUpdateForm, SeekerRegisterForm
from blood.models import Blood
from .models import donor
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        formd = DonorRegisterForm(data=request.POST)
        if form.is_valid() and formd.is_valid():
            user = form.save()
            user.save()
            profile = formd.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created you can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        formd = DonorRegisterForm()

    context={
            'form':form, 'formd':formd
        }
    return render(request, 'users/register.html', context)

def seeker_register(request):
    if request.method == 'POST':
        form = SeekerRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created you can now login.')
            return redirect('transaction')
    else:
        form = SeekerRegisterForm()

    context={
            'form':form
        }
    return render(request, 'users/seeker_register.html', context)

@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        d_form = DonorUpdateForm(request.POST, instance=request.user.donor)
        if u_form.is_valid and d_form.is_valid:
            u_form.save()
            d_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        d_form = DonorUpdateForm(instance=request.user.donor)

    context = {
            'u_form' : u_form,
            'd_form' : d_form
        }
    return render(request, 'users/update_profile.html', context)

@login_required
def profile(request):
    username = request.user.id
    x = Blood.objects.filter(Donor__user=username).order_by('-date_collected')
    context = {'reports':x}
    return render(request, 'users/profile.html', context)