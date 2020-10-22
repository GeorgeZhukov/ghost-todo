from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from django.db import models

from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken import views
from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework as filters
import django_filters




from .models import Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer

# ViewSets define the view behavior.

class ProjectFilter(filters.FilterSet):
 

    class Meta:
        model = Task
        fields = ['name','project__name']
        
    
        #Customise filter generation 
        filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,

                 'extra': lambda f:{
                     'lookup_expr': 'icontains',
                     'lookup_expr': 'endswith',
                 },
             },
        }


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset.filter(id=self.request.user.id)

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer



    def get_queryset(self):
        return self.request.user.projects.all().order_by('-created_at')


class TaskViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,]

    filterset_class = ProjectFilter

    ordering_fields = ['project','project__name', 'name',]


    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)


