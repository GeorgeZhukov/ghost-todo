from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Project


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'owner', 'name', 'created_at']