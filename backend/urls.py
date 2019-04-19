from backend import views
from backend.users import views as users_views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, include

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', include('backend.users.urls'))
])