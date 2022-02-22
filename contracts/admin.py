from django.contrib import admin
from import_export import resources
from .models import Contract
from import_export.admin import ImportExportModelAdmin
from attachments.admin import AttachmentInlines


class ContractResource(resources.ModelResource):

    class Meta:
        model = Contract


class ContractAdmin(ImportExportModelAdmin):
    list_display = ( 
        'name', 'code', 'date', 'sign_date', 'client', 'statement',
    )
    search_fields = (
        'name', 'code', 'date', 'sign_date', 'client__code', 'client__name',
        'statement__name',
    ) 
    list_filter = ('client', 'date', 'sign_date')
    fieldsets = [
                    (
                        None,
                        {
                            'fields': ('code', 'name')
                        }
                    ),
                    (
                        None,
                        {
                            'fields': ('date', 'sign_date')
                        }
                    ),
                    (
                        None,
                        {
                            'fields': ('client', 'statement')
                        }
                    ),

                ]

    # can import or export a contract into database
    resource_class = ContractResource
    # can attach a document of reference
    inlines = (AttachmentInlines,)

# TODO: on delete, delete files inside media directory


admin.site.register(Contract, ContractAdmin)