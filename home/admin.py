from django.contrib import admin
from .models import Maktablar

class MaktablarAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug'),
        }),
    )
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}  

admin.site.register(Maktablar, MaktablarAdmin)