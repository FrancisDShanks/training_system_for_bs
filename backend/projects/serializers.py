from rest_framework import serializers
from .models import Project, Activity, Material


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


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:material-detail")
    owner = serializers.HyperlinkedRelatedField(view_name="backend:userprofile-detail", read_only=True)
    activity = serializers.HyperlinkedRelatedField(many=True, view_name="backend:activity-detail", read_only=True)

    class Meta:
        model = Material
        fields = (
            'url',
            'name',
            'introduction',
            'created_time',
            'owner',
            'resource',
            'activity'
        )


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:activity-detail")
    project = serializers.HyperlinkedRelatedField(view_name="backend:project-detail", read_only=True)
    # material = MaterialSerializer(many=True, read_only=True)
    material = serializers.HyperlinkedIdentityField(many=True, view_name="backend:material-detail")
    # material = serializers.HyperlinkedRelatedField(many=True, view_name="backend:material-detail", queryset=Material.objects.all())


    class Meta:
        model = Activity
        fields = (
            'url',
            'id',
            'name',
            'project',
            'created_time',
            'start_time',
            'end_time',
            'outline',
            'introduction',
            'activity_type',
            'details',
            'material'
        )
