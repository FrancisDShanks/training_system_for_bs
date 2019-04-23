from rest_framework import serializers
from .models import Project, Activity


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:project-detail")
    organization = serializers.HyperlinkedRelatedField(view_name="backend:organization-detail", read_only=True)
    activity = serializers.HyperlinkedIdentityField(many=True, view_name="backend:activity-detail")

    class Meta:
        model = Project
        fields = (
            'url',
            'id',
            'name',
            'start_time',
            'end_time',
            'organization',
            'location',
            'introduction',
            'activity'
        )


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:activity-detail")
    project = serializers.HyperlinkedRelatedField(view_name="backend:project-detail", read_only=True)

    class Meta:
        model = Activity
        fields = (
            'url',
            'id',
            'name',
            'project',
            'start_time',
            'end_time',
            'activity_type',
            'details'
        )