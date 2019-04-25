from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivitySerializer, MaterialSerializer
from .models import Project, Activity, Material
from .filter import ActivityFilter
from rest_framework import filters
from django_filters import rest_framework

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_time')
    serializer_class = ProjectSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-created_time')
    serializer_class = ActivitySerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter,)
    filter_class = ActivityFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'start_time', 'activity_type', 'project')
    #ordering = ('-created_time',)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('-created_time')
    serializer_class = MaterialSerializer