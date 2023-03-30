from django.contrib import admin
from .models import Users, files_upload, Sinitres


@admin.register(Users, files_upload, Sinitres)
class GenericAdmin(admin.ModelAdmin):
    pass