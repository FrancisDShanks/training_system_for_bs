from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, OrganizationSerializer
from .models import UserProfile, Organization
# Create your views here.


class UserList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class OrgList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrgDetail(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer