from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    search_fields = ('first_name', )
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name', )
    list_editable = (
        'birthday',
        'last_name',
    )
    list_filter = ('birthday', )
    empty_value_display = '-пусто-'


admin.site.register(Birthday, BirthdayAdmin)
