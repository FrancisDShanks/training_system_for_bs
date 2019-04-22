from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include

'''
router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'orgs', views.OrganizationViewSet)

urlpatterns = [

    path('', include(router.urls)),

]
'''

'''
urlpatterns += [
    path('apt-auth/', include('rest_framework.urls')),
]
'''