from rest_framework import serializers
from .models import UserProfile, Organization


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # 太坑了！
    url = serializers.HyperlinkedIdentityField(view_name="backend:users:userprofile-detail")
    organization = serializers.HyperlinkedRelatedField(view_name='backend:users:organization-detail', read_only=True)

    class Meta:
        model = UserProfile
        fields = ('url',
                  'id',
                  'chinese_name',
                  'english_name',
                  'created_time',
                  'company_id',
                  'position',
                  'email',
                  'phone',
                  'department',
                  'organization'
                  #'user'
                  )


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:users:organization-detail")
    # user_profile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    user_profile = serializers.HyperlinkedRelatedField(many=True, view_name='backend:users:userprofile-detail', read_only=True)

    class Meta:
        model = Organization
        fields = ('url', 'id', 'name', 'user_profile')