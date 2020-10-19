from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken import views

from .models import Project
from .serializers import ProjectSerializer, UserSerializer

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset.filter(id=self.request.user.id)

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

    


