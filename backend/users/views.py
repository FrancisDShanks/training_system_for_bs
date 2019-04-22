from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from .serializers import UserProfileSerializer, OrganizationSerializer
from .models import UserProfile, Organization
from rest_framework import viewsets

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


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
