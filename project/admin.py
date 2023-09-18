from django.contrib import admin

from .models import IfcTask, IfcRelSequence, IfcTaskTime

# Register your models here.


class IfcProjectAdmin(admin.ModelAdmin):
    model = IfcTask
    list_display = ['Name']


class IfcRelSequenceAdmin(admin.ModelAdmin):
    model = IfcRelSequence
    list_display = []


class IfcTaskTimeAdmin(admin.ModelAdmin):
    model = IfcTaskTime


admin.site.register(IfcTaskTime, IfcTaskTimeAdmin)
admin.site.register(IfcTask, IfcProjectAdmin)
admin.site.register(IfcRelSequence, IfcRelSequenceAdmin)
