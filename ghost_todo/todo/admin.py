from django.contrib import admin

from .models import Project, Task, UserProfile

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('owner',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_filter = ('project', 'project__owner', )
  search_fields = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  pass