from django.contrib import admin
from .models import GroceryItem, MealPlan, TodoItem, TrackedStock

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'completed', 'added_at')
    list_filter = ('completed', 'added_at')
    search_fields = ('name', 'user__username')

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal')
    list_filter = ('date',)
    search_fields = ('meal', 'user__username')
    ordering = ('-date',)

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('text', 'user__username')

@admin.register(TrackedStock)
class TrackedStockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'user')
    search_fields = ('symbol', 'user__username')