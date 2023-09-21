from django.contrib import admin

from .models import IfcTask, IfcRelSequence, IfcTaskTime

# Register your models here.

# Check if these names are the right way around....


class PredecessorRelSequenceInline(admin.TabularInline):
    model = IfcRelSequence
    extra = 0
    fk_name = 'RelatingProcess'
    verbose_name_plural = 'Predecessor Processes'


class SuccessorRelSequenceInline(admin.TabularInline):
    model = IfcRelSequence
    extra = 0
    fk_name = 'RelatedProcess'
    verbose_name_plural = 'Sucessor Processes'


class IfcTaskAdmin(admin.ModelAdmin):
    model = IfcTask
    list_display = ['Name']
    inlines = [PredecessorRelSequenceInline, SuccessorRelSequenceInline, ]


class IfcRelSequenceAdmin(admin.ModelAdmin):
    model = IfcRelSequence
    list_display = []


class IfcTaskTimeAdmin(admin.ModelAdmin):
    model = IfcTaskTime


admin.site.register(IfcTaskTime, IfcTaskTimeAdmin)
admin.site.register(IfcTask, IfcTaskAdmin)
admin.site.register(IfcRelSequence, IfcRelSequenceAdmin)
