from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views

from .models import Project
from .serializers import UserSerializer, ProjectSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer