from django.contrib import admin
from .models import Users, files_upload, Sinistres


@admin.register(Users, files_upload, Sinistres)
class GenericAdmin(admin.ModelAdmin):
    pass