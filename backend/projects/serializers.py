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

    def validate(self, data):
        print(data)
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('end time must later than start time')

        return data


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
    project = serializers.HyperlinkedRelatedField(view_name="backend:project-detail", queryset=Project.objects.all())
    # material = MaterialSerializer(many=True, read_only=True)
    material = serializers.HyperlinkedRelatedField(many=True, view_name="backend:material-detail", queryset=Material.objects.all())


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

    def validate(self, data):
        print(data)
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('end time must later than start time')
        self._check_detail(data)
        return data

    @staticmethod
    def _check_detail(data):
        if data['activity_type'] == 'S':
            keys = set(data['details'].keys())
            if not keys == set(['topic', 'length', 'location', 'teacher', 'audient']):
                raise serializers.ValidationError('the detail of Study activity is invalid.')
            if not isinstance(data['details']['length'], (int, float))\
                    or data['details']['length'] <= 0:
                raise serializers.ValidationError('In Study activity details field, length must be an positive number.')
        elif data['activity_type'] == 'O':
            keys = set(data['details'].keys())
            if not keys == set(['topic', 'length', 'teacher', 'audient']):
                raise serializers.ValidationError('the detail of Online-Study activity is invalid.')
            if not isinstance(data['details']['length'], (int, float))\
                    or data['details']['length'] <= 0:
                raise serializers.ValidationError('In Online-Study activity details field, length must be an positive number.')
        elif data['activity_type'] == 'A':
            keys = set(data['details'].keys())
            if not keys == set(['guest', 'location']):
                raise serializers.ValidationError('the detail of Activity activity is invalid.')
        else:
            raise serializers.ValidationError('the activity type is invalid.')