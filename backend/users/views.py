from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from .serializers import OrganizationSerializer, UserProfileSerializer
from .models import Organization, UserProfile
from rest_framework import viewsets
from .filter import UserProfileFilter, OrganizationFilter
from rest_framework import filters
from django_filters import rest_framework as django_filter_rest_framework
from rest_framework import mixins

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user-profile': reverse('backend:userprofile-list', request=request, format=format),
        'organizaion': reverse('backend:organization-list', request=request, format=format)
    })


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (django_filter_rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProfileFilter
    search_fields = ('chinese_name', 'company_id')
    ordering_fields = ('id', 'chinese_name', 'company_id', 'created_time')
    ordering = ('id',)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (django_filter_rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = OrganizationFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'created_time')
    ordering = ('name',)

