import django_filters
from .models import OneTimeCode


class OneTimeCodeFilter(django_filters.FilterSet):
    class Meta:
        model = OneTimeCode
        fields = ['code']