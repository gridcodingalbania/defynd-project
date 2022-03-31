from django.contrib import admin
from .models import KPI
from statistics_page.models import Statistics

# Register your models here.
class KPIAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        response = Statistics.objects.all()
        extra_context = extra_context or {"statistics": response}
        return super(KPIAdmin, self).changelist_view(
            request, extra_context=extra_context,
        )

    list_display = (
        'contenziosi_in_gestione', 'contenziosi_definiti', 'contenziosi_aperti', 'contenziosi_trattativa',
        'valore_iniziale_totale', 'valore_obiettivo_totale', 'valore_obiettivo_totale_in_trattativa',
        'percentuale_di_incremento', 'ebit_da',
        'any_messi'
    )


admin.site.register(KPI, KPIAdmin)
