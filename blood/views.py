from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Blood, CRYO, FFP, WB, PC, PRBC
from users.models import donor
from django.contrib.auth.models import User
from .filters import UserFilter, city
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'blood/home.html')

def DonorList(request):
    user_list = donor.objects.all().order_by('user__first_name')
    user_filter = UserFilter(request.GET, queryset=user_list).qs
    X = city(request.GET, queryset=user_filter).qs

    page = request.GET.get('page', 1)
    paginator = Paginator(X, 7)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'filter': user_filter, 'users': users, 'X': X,}
    return render(request, 'blood/donors.html', context)

def Blood_stock(request):
    wba = WB.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '+', blood__seeker__isnull = True)
    wbb = WB.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '-', blood__seeker__isnull = True)
    wbc = WB.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '+', blood__seeker__isnull = True)
    wbd = WB.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '-', blood__seeker__isnull = True)
    wbe = WB.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '+', blood__seeker__isnull = True)
    wbf = WB.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '-', blood__seeker__isnull = True)
    wbg = WB.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '+', blood__seeker__isnull = True)
    wbh = WB.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '-', blood__seeker__isnull = True)
    prbca = PRBC.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '+', blood__seeker__isnull = True)
    prbcb = PRBC.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '-', blood__seeker__isnull = True)
    prbcc = PRBC.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '+', blood__seeker__isnull = True)
    prbcd = PRBC.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '-', blood__seeker__isnull = True)
    prbce = PRBC.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '+', blood__seeker__isnull = True)
    prbcf = PRBC.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '-', blood__seeker__isnull = True)
    prbcg = PRBC.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '+', blood__seeker__isnull = True)
    prbch = PRBC.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '-', blood__seeker__isnull = True)
    pca = PC.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '+', blood__seeker__isnull = True)
    pcb = PC.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '-', blood__seeker__isnull = True)
    pcc = PC.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '+', blood__seeker__isnull = True)
    pcd = PC.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '-', blood__seeker__isnull = True)
    pce = PC.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '+', blood__seeker__isnull = True)
    pcf = PC.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '-', blood__seeker__isnull = True)
    pcg = PC.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '+', blood__seeker__isnull = True)
    pch = PC.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '-', blood__seeker__isnull = True)
    ffpa = FFP.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '+', blood__seeker__isnull = True)
    ffpb = FFP.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '-', blood__seeker__isnull = True)
    ffpc = FFP.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '+', blood__seeker__isnull = True)
    ffpd = FFP.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '-', blood__seeker__isnull = True)
    ffpe = FFP.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '+', blood__seeker__isnull = True)
    ffpf = FFP.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '-', blood__seeker__isnull = True)
    ffpg = FFP.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '+', blood__seeker__isnull = True)
    ffph = FFP.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '-', blood__seeker__isnull = True)
    cryoa = CRYO.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '+', blood__seeker__isnull = True)
    cryob = CRYO.objects.filter(status =True, blood__Blood_Group = 'O', blood__Rh_factor = '-', blood__seeker__isnull = True)
    cryoc = CRYO.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '+', blood__seeker__isnull = True)
    cryod = CRYO.objects.filter(status =True, blood__Blood_Group = 'A', blood__Rh_factor = '-', blood__seeker__isnull = True)
    cryoe = CRYO.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '+', blood__seeker__isnull = True)
    cryof = CRYO.objects.filter(status =True, blood__Blood_Group = 'B', blood__Rh_factor = '-', blood__seeker__isnull = True)
    cryog = CRYO.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '+', blood__seeker__isnull = True)
    cryoh = CRYO.objects.filter(status =True, blood__Blood_Group = 'AB', blood__Rh_factor = '-', blood__seeker__isnull = True)
    context = {
        'wba':wba, 'wbb':wbb, 'wbc':wbc, 'wbd':wbd, 'wbe':wbe, 'wbf':wbf, 'wbg':wbg, 'wbh':wbh,
        'prbca':prbca, 'prbcb':prbcb, 'prbcc':prbcc, 'prbcd':prbcd, 'prbce':prbce, 'prbcf':prbcf, 'prbcg':prbcg, 'prbch':prbch,
        'pca':pca, 'pcb':pcb, 'pcc':pcc, 'pcd':pcd, 'pce':pce, 'pcf':pcf, 'pcg':pcg, 'pch':pch,
        'ffpa':ffpa, 'ffpb':ffpb, 'ffpc':ffpc, 'ffpd':ffpd, 'ffpe':ffpe, 'ffpf':ffpf, 'ffpg':ffpg, 'ffph':ffph,
        'cryoa':cryoa, 'cryob':cryob, 'cryoc':cryoc, 'cryod':cryod, 'cryoe':cryoe, 'cryof':cryof, 'cryog':cryog, 'cryoh':cryoh,
    }
    return render(request, 'blood/blood_stock.html', context)

def date(request):
    A = Blood.objects.all()
    wb = WB.objects.all()
    prbc = PRBC.objects.all()
    ffp = FFP.objects.all()
    pc = PC.objects.all()
    cryo = CRYO.objects.all()
    for i in A:
        x=0
        if i.seeker:
            x=1
        for j in wb:
            print(i.id, i.date_collected, j.blood, j.status, j)
            a = str(j.blood)
            b= str(i.id)
            if a == b and j.status == True:
                dt = timezone.now() - i.date_collected
                print(dt)
                if dt.days > 35 or x==1:
                    j.status = False
                    j.save()
        for k in prbc:
            print(i.id, i.date_collected, k.blood, k.status, k)
            a = str(k.blood)
            b= str(i.id)
            if a == b and k.status == True:
                dt = timezone.now() - i.date_collected
                print(dt)
                if dt.days > 42 or x==1:
                    k.status = False
                    k.save()
        for l in ffp:
            print(i.id, i.date_collected, l.blood, l.status, l)
            a = str(l.blood)
            b= str(i.id)
            if a == b and l.status == True:
                dt = timezone.now() - i.date_collected
                print(dt)
                if dt.days > 365 or x==1:
                    l.status = False
                    l.save()
        for m in pc:
            print(i.id, i.date_collected, m.blood, m.status, m)
            a = str(m.blood)
            b= str(i.id)
            if a == b  and m.status == True:
                dt = timezone.now() - i.date_collected
                print(dt)
                if dt.days > 5 or x==1:
                    m.status = False
                    m.save()
        for n in cryo:
            print(i.id, i.date_collected, n.blood, n.status, n)
            a = str(n.blood)
            b= str(i.id)
            if a == b  and n.status == True:
                print(dt)
                dt = timezone.now() - i.date_collected
                if dt.days > 365 or x==1:
                    n.status = False
                    n.save()
    messages.success(request, f'Blood Stock Updated')
    return Blood_stock(request)

def Products(request):
    return render(request, "blood/products.html") 