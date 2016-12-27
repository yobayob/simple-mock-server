from django.contrib import admin
from public.models import *
# Register your models here.


class FlatPageAdmin(admin.ModelAdmin):
    can_delete = False
    readonly_fields=('type',)

    def has_add_permission(self, request):
        return False

admin.site.register(Personal)
admin.site.register(FlatPage, FlatPageAdmin)
