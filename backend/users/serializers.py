from rest_framework import serializers
from .models import UserProfile, Organization


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:userprofile-detail")
    organization = serializers.HyperlinkedRelatedField(view_name='backend:organization-detail',
                                                       queryset=Organization.objects.all())
    #user = serializers.HyperlinkedRelatedField(view_name='backend:user-detail', queryset=User.objects.all())


    class Meta:
        model = UserProfile
        fields = ('url',
                  'id',
                  'username',
                  'chinese_name',
                  'english_name',
                  'created_time',
                  'gender',
                  'company_id',
                  'position',
                  'email',
                  'phone',
                  'department',
                  'organization'
                  )


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="backend:organization-detail")
    # user_profile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    user_profile = serializers.HyperlinkedRelatedField(many=True, view_name='backend:userprofile-detail', read_only=True)

    class Meta:
        model = Organization
        fields = ('url', 'id', 'name', 'user_profile')


