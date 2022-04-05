from django.contrib import admin
from .models import KPI
from statistics_page.models import Statistics
from django.utils.translation import ugettext_lazy as _

# Register your models here.
class KPIAdmin(admin.ModelAdmin):
    # admin.site.site_header = 'My Site Admin Panel'
    # admin.site.site_title = 'My Site Title'
    actions = None

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        response = Statistics.objects.all()
        extra_context = extra_context or {"statistics": response}
        extra_context["initial_total_value"] = _("initial_total_value")
        # extra_context["initial_total_value"] = _("initial_total_value")
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


admin.site.site_header = "Kpi"
# admin.site.index_title = " "
# admin.site.site_title = " "
# admin.site.header = " "