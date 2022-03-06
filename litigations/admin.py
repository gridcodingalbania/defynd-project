from django.contrib import admin
from .models import Litigation
from django.utils.translation import gettext_lazy as _
from .forms import LitigationForm
from django import forms
from statistics_page.models import Statistics
from decimal import Decimal


class LitigationAdmin(admin.ModelAdmin):
    __currency_variables = ["initial_estimation_value"]
    list_display = (
        'name', 'time', 'client', 'dispute_matter',
        'dispute_object', 'initial_estimation_value', 'target_value',
        'registration_type', 'closed', 'origin',
    )
    # filter in the right side of the list appearance
    list_filter = (
        'time', 'dispute_matter', 'dispute_object', 'registration_type', 'lawyer_reference',
        'area_address', 'reception_act', 'date_receipt_act', 'purchase_contract',
        'contract_date', 'culture_type', 'fruit_pendants',
        'cultivator_type', 'social_economic_reform', 'urban_destination',
        'epoch_construction', 'purchase_contract', 'contract_date',
        'purchase_contract', 'residual_airspace',
        'storage_state', 'lease_agreement', 'contract_duration',
        'residual_rent', 'reclamation_intervention_type', 'closed'
    )
    # search box appearance
    search_fields = (
        'name', 'client__code', 'client__name',
    )

    fieldsets = [
        (
            None,
            {
                'fields': (('name', 'closed'),
                           'client', 'hyperlink', 'upload_pdf'),
            }
        ),
        (
            _('Reference'),
            {
                'fields': ('lawyer_reference', 'reference',)
            }
        ),
        (
            _('Other Information'),
            {
                'fields': (
                    'reception_act', 'date_receipt_act',
                    'purchase_contract', 'contract_date',

                ),
                'classes': ('wide',)
            }
        ),
        (
            _('Dispute'),
            {
                'fields': ('dispute_matter', 'dispute_object',
                           'starting_date', 'target_date', 'closing_date'),
                'classes': ('wide', 'extrapretty')
            }
        ),
        (
            _('Value'),
            {
                'fields': ('initial_estimation_value', 'target_value', 'final_value',
                           'revenue', 'total_cost', 'turnover_margin'),
                'classes': ('wide', 'extrapretty')
            }
        ),
        (
            _('Registration'),
            {
                'fields': ('registration_type', 'prejudicial_registrations', 'enrollment_amount',),
                'classes': ('wide', 'extrapretty')
            }
        ),
        (
            _('Area'),
            {
                'fields': (('surface_directly_concerned', 'occupied_area', 'residual_surface',),
                           'area_address', 'technical_reference',),
                'classes': ('wide', 'extrapretty')
            }
        ),
        (
            _('Information Culture'),
            {
                'fields': (('culture_type',),  # 'area_type',
                           'aboveground_quantification',
                           'fruit_pendants', 'cultivator_type', 'batch_disfiguration',
                           'description',),
                'classes': ('wide', 'esproprio_agricolo',),
            }
        ),
        (
            _('Free Residential Industrial Expropriation'),
            {
                'fields': (('social_economic_reform', 'urban_destination',),
                           ('transformation_coefficient', 'IMU_final_declaration',),),
                'classes': ('wide', 'esproprio_residenziale'),
            }
        ),
        (
            _('Expropriation Residential Industrial Building'),
            {
                'fields': (
                    ('epoch_construction', 'building_titles',),
                    ('extension_MQ', 'residual_airspace', 'MC_residui',),
                    ('total_demolition', 'partial_demolition',),
                    ('storage_state', 'productive_activities',),
                    ('lease_agreement', 'contract_duration',),
                    ('contract_fee', 'residual_rent',),
                    ('need_transfer_user', 'reclamation_activities',),
                    ('reclamation_intervention_type', 'reclamation_cost',),
                ),
                'classes': ('wide', 'esproprio_fabbricato',),
            }
        ),

    ]

    def __updateCurrencyValues(self, post_form):
        temp = post_form.copy()
        for currency_variable in self.__currency_variables:
            if currency_variable in temp:
                if temp[currency_variable] == "":
                    temp[currency_variable] = 0
                else:
                    temp[currency_variable] = self.__removeCommas(temp[currency_variable])
        return temp

    def __removeCommas(self, form_variable):
        splited_values = form_variable.split(",")
        string_number = "".join(splited_values)
        number = Decimal(string_number)
        return number

    # def save_model(self, request, obj, form, change):
    #     # update_statistics_data(form.cleaned_data)
    #     request.POST = self.__updateCurrencyValues(request.POST)
    #     form = LitigationForm(request.POST)
    #     if form.is_valid():
    #         record = form.save()
    #         record.save()

    def clean(self):
        return self.cleaned_data

    # all required=True information in litigation form, will be requried also in the admin model
    form = LitigationForm

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(
            request, object_id, form_url,
        )

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
            'admin/js/litigation.js',  # project static folder
            'js/litigation.js'
        )


# def update_gestione_statistic(litigation_data, id):
#     try:
#         statistic = Statistics.objects.get(id=id)
#         if litigation_data["initial_estimation_value"]:
#             statistic.initial_value += float(litigation_data["initial_estimation_value"])
#
#         if litigation_data["target_value"]:
#             statistic.objective_value += float(litigation_data["target_value"])
#
#         if litigation_data["final_value"]:
#             statistic.final_value += float(litigation_data["final_value"])
#
#         if litigation_data["revenue"]:
#             statistic.revue_value += float(litigation_data["revenue"])
#
#         if litigation_data["total_cost"]:
#             statistic.total_cost_value += float(litigation_data["total_cost"])
#
#         if litigation_data["turnover_margin"]:
#             statistic.margin_value += float(litigation_data["turnover_margin"])
#
#         if statistic.initial_value != 0:
#             statistic.total_value = round(statistic.final_value / statistic.initial_value, 2)
#         else:
#             statistic.initial_value = 0
#         statistic.save()
#     except Statistics.DoesNotExist:
#         pass
#
#
# def update_statistics_data(litigation_data):
#     litigation_is_closed = litigation_data["closed"]
#     litigation_is_opened = not litigation_is_closed
#     contract_uploaded = litigation_data["upload_pdf"] is not None
#     contract_not_uploaded = not contract_uploaded
#
#     # Update Gestione Statistic
#     update_gestione_statistic(litigation_data, 1)
#
#     if litigation_is_closed and contract_uploaded:
#         update_gestione_statistic(litigation_data, 2)
#     elif litigation_is_opened and contract_uploaded:
#         update_gestione_statistic(litigation_data, 3)
#     elif litigation_is_opened and contract_not_uploaded:
#         update_gestione_statistic(litigation_data, 4)





admin.site.register(Litigation, LitigationAdmin)
# Change Site header and title
admin.site.site_header = "Litigation Management System"
admin.site.index_title = "Litigation Management System"
admin.site.site_title = "DEFYND"
admin.site.header = "DEFYND"
