import django_filters
from .models import *


class ActivityFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    start_time = django_filters.DateTimeFromToRangeFilter(field_name='start_time')
    # TODO: ChoiceFilter
    activity_type = django_filters.CharFilter(field_name='activity_type', lookup_expr='icontains')
    project = django_filters.NumberFilter(field_name='project')

    class Meta:
        model = Activity
        fields = ['name', 'start_time', 'activity_type', 'project']


class ProjectFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    start_time = django_filters.DateTimeFromToRangeFilter(field_name='start_time')
    end_time = django_filters.DateTimeFromToRangeFilter(field_name='end_time')
    cost_gte = django_filters.NumberFilter(field_name='cost', lookup_expr='gte')
    cost_lte = django_filters.NumberFilter(field_name='cost', lookup_expr='lte')
    cost_budget_gte = django_filters.NumberFilter(field_name='cost_budget', lookup_expr='gte')
    cost_budget_lte = django_filters.NumberFilter(field_name='cost_budget', lookup_expr='lte')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    # TODO: acitity filter
    # TODO: manager and creator filter

    class Meta:
        model = Project
        fields = ['name', 'start_time', 'end_time', 'cost_gte', 'cost_lte', 'cost_budget_gte', 'cost_budget_lte',
                  'cost_budget', 'price_gte', 'price_lte', 'location']