from django.contrib import admin

from .models import CSPDirective, CSPDirectiveValue


class CSPDirectiveValueInline(admin.TabularInline):
    model = CSPDirectiveValue


@admin.register(CSPDirective)
class CSPDirectiveAdmin(admin.ModelAdmin):

    @classmethod
    def joined_values(cls, obj):
        return ', '.join([v.value for v in obj.directive_values.all()])
    joined_values.short_description = 'Values'

    list_display = ('name', 'joined_values')
    inlines = [
        CSPDirectiveValueInline,
    ]
