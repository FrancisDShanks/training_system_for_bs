from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivitySerializer, MaterialSerializer
from .models import Project, Activity, Material

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_time')
    serializer_class = ProjectSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-created_time')
    serializer_class = ActivitySerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('-created_time')
    serializer_class = MaterialSerializer