from django.contrib import admin
from django.contrib import admin

from todo.models import *

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('owner',)
    search_fields = ('name',)



