from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, include

urlpatterns = [
    path('org/', OrgList.as_view(), name='org-list'),
    path('org/<int:pk>/', OrgDetail.as_view(), name='org-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail')
]