from django.contrib import admin
from .models import CultureType, UrbanDestination, ReclamationInterventionType, AreaType, ConstraintType, DisputeMatter, DisputeObject


class AreaTypeAdmin(admin.ModelAdmin): 
    list_display = (
        'name',
    )


class ConstraintTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CultureTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ReclamationInterventionTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class UrbanDestinationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class DisputeMatterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class DisputeObjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(ConstraintType, ConstraintTypeAdmin)
admin.site.register(CultureType, CultureTypeAdmin)
admin.site.register(ReclamationInterventionType, ReclamationInterventionTypeAdmin)
admin.site.register(AreaType, AreaTypeAdmin)
admin.site.register(UrbanDestination, UrbanDestinationAdmin)
admin.site.register(DisputeMatter, DisputeMatterAdmin)
admin.site.register(DisputeObject, DisputeObjectAdmin)
