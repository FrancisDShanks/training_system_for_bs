from rest_framework import serializers
from .models import UserProfile, Organization
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # 太坑了！
    url = serializers.HyperlinkedIdentityField(view_name="backend:userprofile-detail")
    organization = serializers.HyperlinkedRelatedField(view_name='backend:organization-detail',
                                                       queryset=Organization.objects.all())
    user = serializers.HyperlinkedRelatedField(view_name='backend:user-detail', queryset=User.objects.all())

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
                  'organization',
                  'user'
                  )


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:organization-detail")
    # user_profile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    user_profile = serializers.HyperlinkedRelatedField(many=True, view_name='backend:userprofile-detail', read_only=True)

    class Meta:
        model = Organization
        fields = ('url', 'id', 'name', 'user_profile')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:user-detail")
    user_profile = serializers.HyperlinkedRelatedField(view_name='backend:userprofile-detail',
                                                       read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'is_staff', 'user_profile')