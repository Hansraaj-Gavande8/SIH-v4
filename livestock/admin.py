from django.contrib import admin
from .models import Farm, Livestock

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name']

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ['tag_number', 'farm', 'species']
    list_filter = ['species']
    search_fields = ['tag_number']
