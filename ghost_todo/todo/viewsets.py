from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken import views
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def current_user(self, request):
        current_user = self.request.user

        serializer = self.get_serializer(current_user, many=False)
        return Response(serializer.data)

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all().order_by('-created_at')


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', ]

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)
