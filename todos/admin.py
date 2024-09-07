from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'owner', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'owner')
    search_fields = ('title', 'description')

# If you are not using the decorator, you can register the model like this:
# admin.site.register(Todo, TodoAdmin)
