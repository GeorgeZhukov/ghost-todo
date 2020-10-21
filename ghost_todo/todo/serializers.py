from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Project, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'id', 'owner', 'name', 'created_at']
        read_only_fields = ['owner']

    def create(self, validated_data):
        user = self.context['request'].user

        return user.projects.create(**validated_data)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [ 'id', 'name', 'created_at', 'project']
