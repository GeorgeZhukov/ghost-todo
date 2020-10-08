from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
  owner = models.ForeignKey(User, on_delete=models.RESTRICT)
  name = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


