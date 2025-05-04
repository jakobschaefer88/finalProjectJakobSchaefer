from django.contrib import admin
from .models import TrackedStock

@admin.register(TrackedStock)
class TrackedStockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'user')
    search_fields = ('symbol', 'user__username')