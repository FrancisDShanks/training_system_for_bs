import django_filters
from .models import *


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    chinese_name = django_filters.CharFilter(field_name='chinese_name', lookup_expr='icontains')
    english_name = django_filters.CharFilter(field_name='english_name', lookup_expr='icontains')
    company_id = django_filters.NumberFilter(field_name='company_id')


    class Meta:
        model = UserProfile
        fields = ['chinese_name', 'english_name']


class OrganizationFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Organization
        fields = ['name']