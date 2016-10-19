from django.contrib import admin

from .models import Department, Workcell, Equipment, CommunicationType,\
    ControllerType, Controller, PointType, Rack, Point


class WorkcellInLine(admin.StackedInline):
    model = Workcell
    extra = 2


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [WorkcellInLine]


class EquipmentInLine(admin.StackedInline):
    model = Equipment.workcell.through
    extra = 2


class WorkcellAdmin(admin.ModelAdmin):
    inlines = [EquipmentInLine]


class RackInLine(admin.StackedInline):
    model = Rack
    extra = 8


class ControllerAdmin(admin.ModelAdmin):
    inlines = [RackInLine]


class PointInLine(admin.StackedInline):
    model =

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Workcell, WorkcellAdmin)
admin.site.register(Equipment)
admin.site.register(CommunicationType)
admin.site.register(ControllerType)
admin.site.register(PointType)
admin.site.register(Controller, ControllerAdmin)