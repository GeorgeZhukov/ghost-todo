from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here


class Project(models.Model):
  owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='projects')
  name = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}'.format(self.name)


class Task(models.Model):
  project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  deadline = models.DateTimeField(blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}'.format(self.name)



