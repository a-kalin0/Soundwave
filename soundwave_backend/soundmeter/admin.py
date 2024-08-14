from django.contrib import admin
from .models import Sound

# Register your models here.

@admin.register(Sound)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'duration', 'created_at']
    search_fields = ['title', 'duration']
    list_filter = ['duration', 'max_db_size', 'avg_db_size', 'created_at']