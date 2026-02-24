from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',) # Najnowsze na górze
