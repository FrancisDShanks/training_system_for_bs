from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .users import views as users_view
from .projects import views as projects_view
from rest_framework_jwt.views import obtain_jwt_token
'''
urlpatterns = format_suffix_patterns([

    path('users/', include('backend.users.urls'))
])
'''

router = DefaultRouter()
router.register(r'users', users_view.UserProfileViewSet)
router.register(r'orgs', users_view.OrganizationViewSet)
router.register(r'projects', projects_view.ProjectViewSet)
router.register(r'activities', projects_view.ActivityViewSet)
router.register(r'materials', projects_view.MaterialViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path(r'login/', obtain_jwt_token),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
'''
urlpatterns = [
    path('users/', include(('backend.users.urls', 'backend'), namespace='users'))
    ]
'''