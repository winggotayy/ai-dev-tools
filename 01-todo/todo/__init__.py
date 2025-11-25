'''
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_resolved', 'due_date', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Task Info', {
            'fields': ('title', 'description')
        }),
        ('Dates', {
            'fields': ('due_date', 'created_at', 'updated_at')
        }),
        ('Status', {
            'fields': ('is_resolved',)
        }),
    )
'''

# Leave this file empty or with just default content