from django.contrib import admin

from .models import IfcTask

# Register your models here.


class IfcProjectAdmin(admin.ModelAdmin):
    model = IfcTask
    list_display = ['Name']


admin.site.register(IfcTask, IfcProjectAdmin)
