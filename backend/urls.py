from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, include
'''
urlpatterns = format_suffix_patterns([

    path('users/', include('backend.users.urls'))
])
'''
urlpatterns = [
    path('users/', include(('backend.users.urls', 'backend'), namespace='users'))
    ]