from rest_framework import serializers
from .models import UserProfile, Organization


class UserSerializer(serializers.HyperlinkedModelSerializer):
    org = serializers.HyperlinkedRelatedField(view_name='', read_only=True)

    class Meta:
        model = UserProfile
        fields = ('chinese_name',
                  'created_time',
                  'company_id',
                  'position',
                  'email',
                  'phone',
                  'department',
                  'username')


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(many=True, view_name='', read_only=True)

    class Meta:
        model = Organization
        field = ('name')