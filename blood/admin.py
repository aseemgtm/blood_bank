from django.contrib import admin
from .models import Blood, Transaction, PC, PRBC, WB, CRYO, FFP
import csv

# Register your models here.
admin.site.register(Blood)
admin.site.register(Transaction)
admin.site.register(WB)
admin.site.register(PRBC)
admin.site.register(FFP)
admin.site.register(PC)
admin.site.register(CRYO)