from django.urls import path, include

from django.contrib.auth.models import User

from rest_framework import routers
from rest_framework.authtoken import views

from .viewsets import UserViewSet, ProjectViewSet, TaskViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet,  basename='project')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]
