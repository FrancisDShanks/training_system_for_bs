from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivitySerializer
from .models import Project, Activity
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
