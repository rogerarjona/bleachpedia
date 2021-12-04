from django.contrib import admin
from .models import Shinigami


@admin.register(Shinigami)
class ShinigamiAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name" )