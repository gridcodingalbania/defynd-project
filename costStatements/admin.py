from django.contrib import admin
from .models import Item, CostStatement, CostStatementItem, Hypothesis, ItemCategory
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    fieldsets = [
        (
            None,
            {
                'fields': ('name', 'code')
            }
        )
    ]


class ItemAdmin(admin.ModelAdmin):
    list_display = ('priority', 'name', 'code', 'category')
    search_fields = ('name', 'code', 'category__name')
    list_filter = ('category', )
    fieldsets = [
        (
            None,
            {
                'fields': ('name', 'code', 'priority', 'category')
            }
        )
    ]


class HypothesisAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description'
    )


class CostStatementItemAdmin(admin.ModelAdmin):
    list_display = (
        'item', 'percentage', 'value', 'hypothesis', 'cost_statement'
    )
    search_fields = ('item__name', 'cost_statement__name', 'hypothesis__name')
    list_filter = ('item', 'cost_statement', 'hypothesis')


class CostStatementItemline(admin.TabularInline):
    model = CostStatementItem
    fields = ('item', 'cost_statement', 'percentage', 'value', 'hypothesis')


class CostStatementResource(resources.ModelResource):
    class Meta:
        model = CostStatement


class CostStatementAdmin(ImportExportModelAdmin):
    menu_title = "Cost Statements"
    list_display = ('code', 'name', 'time', 'client', 'litigation', 'init_amount', 'total')
    inlines = [CostStatementItemline]
    fieldsets = [
        (
            None,
            {
                'fields': ('code', )
            }
        ),
        (
            None,
            {
                'fields': ('name', )
            }
        ),
        (
            None,
            {
                'fields': ('litigation', 'client')
            }
        ),
        (
            None,
            {
                'fields': ('init_negotiation', 'expected_dealing_term')
            }
        ),
        (
            None,
            {
                'fields': ('init_amount', 'total')
            }
        ),
    ]
    resource_class = CostStatementResource


admin.site.register(CostStatement, CostStatementAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Hypothesis, HypothesisAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(CostStatementItem, CostStatementItemAdmin)
