from django.contrib import admin
from .models import Statistics
from litigations.models import Litigation
from decimal import Decimal
from .utils import build_statistics_objects


class StatisticAdmin(admin.ModelAdmin):
    actions = None

    def get_queryset(self, request):
        """Use this so we can annotate with additional info."""
        build_statistics_objects()
        qs = super(StatisticAdmin, self).get_queryset(request)
        return qs

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    class Media:
        js = ('js/statistic.js',)

    list_display = (
        'title', 'number', 'initial_value', 'objective_value', 'final_value', 'total_value',
        'revue_value', 'total_cost_value', 'margin_value'
    )


# Register your models here.
admin.site.register(Statistics, StatisticAdmin)
