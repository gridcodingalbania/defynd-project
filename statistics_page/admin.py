from django.contrib import admin
from .models import Statistics


class StatisticAdmin(admin.ModelAdmin):

    class Media:
        js = ('js/statistic.js', )

    list_display = (
        'name', 'initial_value', 'objective_value', 'final_value', 'total_value',
        'revue_value', 'total_cost_value', 'margin_value', 'description'
    )

    fieldsets = [
        (
            None,
            {
                'fields': (('name', ('initial_value', 'objective_value',
                                    'final_value',
                           'total_value', 'revue_value', 'total_cost_value', 'margin_value'),
                           'description')),
            }
        ),

    ]


# Register your models here.
admin.site.register(Statistics, StatisticAdmin)
