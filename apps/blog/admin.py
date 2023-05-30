from django.contrib import admin
from django.utils.html import format_html

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    def imagem_tag(self, obj):
        if obj.imagem:
            return format_html(f"<img src='{obj.imagem.url}'  width='100' height='80' />")
        return ""

    imagem_tag.short_description = "Imagens"

    list_display = ("id", "titulo", "imagem_tag", )
    list_display_links = ("titulo", )
    list_filter = ("titulo", )
    search_fields = ("titulo", )


admin.site.register(Blog, BlogAdmin)
