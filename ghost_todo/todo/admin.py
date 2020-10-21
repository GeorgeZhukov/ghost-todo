from django.contrib import admin

from todo.models import Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('owner',)
    search_fields = ('name',)



