from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", )
    list_filter = ("titulo", )
    search_fields = ("titulo", )

admin.site.register(Blog, BlogAdmin)
