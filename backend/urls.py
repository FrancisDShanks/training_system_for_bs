from backend import views
from backend.users import views as users_views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, include

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('org/',
        users_views.OrgList.as_view(),
        name='org-list'),
    path('org/<int:pk>/',
        users_views.OrgDetail.as_view(),
        name='org-detail'),
    path('users/',
        users_views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        users_views.UserDetail.as_view(),
        name='user-detail')
])
