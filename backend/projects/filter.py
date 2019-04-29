import django_filters
from .models import *


class ActivityFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    start_time = django_filters.DateTimeFromToRangeFilter(field_name='start_time')
    activity_type = django_filters.CharFilter(field_name='activity_type', lookup_expr='icontains')
    project = django_filters.NumberFilter(field_name='project')

    class Meta:
        model = Activity
        fields = ['name', 'start_time', 'activity_type', 'project']


class ProjectFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    start_time = django_filters.DateTimeFromToRangeFilter(field_name='start_time')
    end_time = django_filters.DateTimeFromToRangeFilter(field_name='end_time')

    class Meta:
        model = Project
        fields = ['name', 'start_time', 'end_time']