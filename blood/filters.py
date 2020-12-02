from users.models import donor
import django_filters
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = donor
        fields = ['Blood_Group', 'Rh_factor']

class city(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = donor
        fields = ['city',]

