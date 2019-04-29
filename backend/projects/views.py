from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivitySerializer, MaterialSerializer
from .models import Project, Activity, Material
from backend.users.models import UserProfile
from .filter import ActivityFilter, ProjectFilter
from rest_framework import filters
from django_filters import rest_framework as django_filter_rest_framework

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (django_filter_rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'start_time', 'created_time')
    ordering = ('-created_time',)

    def perform_create(self, serializer):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user.id)
        serializer.save(
            project_manager=user_profile,
            project_creator=user_profile
        )


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (django_filter_rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ActivityFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'start_time', 'activity_type', 'project', 'created_time')
    ordering = ('-created_time',)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('-created_time')
    serializer_class = MaterialSerializer