from django.contrib import admin
from .models import Statistics



class StatisticAdmin(admin.ModelAdmin):
    actions = None
    title = False

    def has_add_permission(self, request, obj=None):
         return False

    class Media:
        js = ('js/statistic.js', )

    list_display = (
         'title', 'number', 'initial_value', 'objective_value', 'final_value', 'total_value',
        'revue_value', 'total_cost_value', 'margin_value'
    )

    fieldsets = [
        (
            None,
            {
                'fields': (('title', ('initial_value', 'objective_value',
                                    'final_value',
                           'total_value', 'revue_value', 'total_cost_value', 'margin_value'),
                           'description')),
            }
        ),

    ]


# Register your models here.
admin.site.register(Statistics, StatisticAdmin)
