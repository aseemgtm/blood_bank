from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home , name='blood-home'),
    #path('transaction/', views.transaction, name='transaction'),
    url(r'^donors/$', views.DonorList, name='donors'),
    path('blood_stock/', views.Blood_stock, name='blood-stock'),
    url(r'^blood_stock/update/$', views.date, name='update'),
    path('products/', views.Products, name = 'products'),
]
