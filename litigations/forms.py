from material import Layout, Row, Fieldset
from django import forms
from configurations.models import *
from lawyers.models import Lawyer
from admin_panel import settings
from litigations.models import Litigation
from clients.models import *
from django.utils.translation import gettext_lazy as _


CHOICES = (
    ('yes', _('yes')),
    ('no', _('no')),
)

VALUES = (
    ('value_1', _('value-1')),
    ('value_2', _('value-2')),
)

storage_choices = (
    ('great', _('great')),
    ('good', _('good')),
    ('enough', _('enough')),
    ('to_be_restructured', _('to-be-restructured')),
)

registration_choices = (
    ('Esproprio Agricolo', _('esproprio-agricolo')),
    ('Esproprio Residenziale Libera', _('esproprio-residenziale-libera')),
    ('Esproprio Industriale Libera', _('esproprio-industriale-libera')),
    ('Esproprio Fabbricato Residenziale', _('esproprio-fabbricato-residenziale')),
    ('Esproprio Fabbricato Industriale', _('esproprio-fabbricato-industriale')),
        ('Area boschiva', _('Area boschiva')),
        ('Area industriale con fabbricati', _('Area industriale con fabbricati')),
        ('Area industriale senza fabbricati', _('Area industriale senza fabbricati')),
        ('Area Residenziale con fabbricati', _('Area Residenziale con fabbricati')),
        ('Area Residenziale senza fabbricati', _('Area Residenziale senza fabbricati')),
        ('Area Agricola con fabbricati', _('Area Agricola con fabbricati')),
        ('Area Agricola senza fabbricati', _('Area Agricola senza fabbricati'))
)


class LitigationForm(forms.ModelForm):
    # The form is used inside admin interface and will block record registration if left required here
    email = forms.EmailField(label=_('e-mail'), required=False)
    closed = forms.BooleanField(required=False)

    # litigation
    dispute_matter = forms.ModelChoiceField(queryset=DisputeMatter.objects.all(),
                                            label=_('Dispute Matter'))
    upload_pdf = forms.FileField(label=_("Upload Contract"), required=False)
    dispute_object = forms.ModelChoiceField(queryset=DisputeObject.objects.all(),
                                            label=_('Dispute Object'))
    initial_estimation_value = forms.CharField(label=_('Initial Estimation Value'), required=False)
    final_value = forms.CharField(label=_('Final Value'), required=False)
    revenue = forms.CharField(label=_('Revenue'), required=False)
    fee_percentuale = forms.CharField(label=_('Fee Percentuale'), required=False)
    total_cost = forms.CharField(label=_('Total Cost'), required=False)
    target_value = forms.CharField(label=_('Target Value'), required=False)
    EBIT = forms.CharField(label=_('Turnover Margin'), required=False)
    closing_date = forms.DateField(label=_('Closing Date'), required=False, help_text="dd/mm/yyyy",  input_formats=settings.DATE_INPUT_FORMATS)
    reference = forms.CharField(label=_('reference'), required=False)
    prejudicial_registrations = forms.CharField(label=_('Prejudicial Registrations'), required=False, )
    registration_type = forms.ChoiceField(label=_('Registration Type'), choices=registration_choices,
                                          widget=forms.Select())
    enrollment_amount = forms.CharField(label=_('Enrollment Amount'), required=False, )
    surface_directly_concerned = forms.FloatField(label=_('Surface Directly Concerned'), required=False, )
    residual_surface = forms.FloatField(label="", required=False, help_text=_('Residual Surface'), disabled=False)
    technical_reference = forms.CharField(label=_('Technical Reference'), required=False,)
    lawyer_reference = forms.ModelChoiceField(queryset=Lawyer.objects.all(),
                                              label=_('Lawyer Reference'), required=False)
    area_address = forms.CharField(label=_('Area Address'), required=False,)
    occupied_area = forms.FloatField(label=_('Occupied Area'), required=False, )
    reception_act = forms.ChoiceField(widget=forms.RadioSelect, label=_('Reception Act'),
                                      choices=CHOICES, required=False, )
    date_receipt_act = forms.DateField(label=_('Date Receipt Act'), required=False, help_text="dd/mm/yyyy", input_formats=settings.DATE_INPUT_FORMATS)
    purchase_contract = forms.CharField(label=_('Purchase Contract'), required=False)
    contract_date = forms.DateField(label=_('Contract Date'),  required=False, help_text="dd/mm/yyyy", input_formats=settings.DATE_INPUT_FORMATS)
    last_notary_fees = forms.CharField(label=_('Last Notary Fees'), required=False, )
    other_constraints_type = forms.ModelChoiceField(queryset=ConstraintType.objects.all(),
                                                    label=_('Other Constraints Type'), required=False, )

    # area_type = forms.ModelChoiceField(queryset=AreaType.objects.all(),
    #     # FIX: widget adds another row with the value
    #     # widget=forms.Select(attrs = {'class': 'esproprio_agricolo'}),
    #     label="Tipologia Area", required=False,)
    culture_type = forms.ModelChoiceField(queryset=CultureType.objects.all(),
                                          # widget=forms.Select(attrs = {'class': 'esproprio_agricolo'}),
                                          label=_('Culture Type'), required=False, )

    above_ground_quantification = forms.CharField(label=_('Above Ground Quantification'), required=False, )

    # fruit_pendants = forms.ChoiceField(label="Frutti Pendenti", choices=CHOICES, widget=forms.Select())
    fruit_pendants = forms.ChoiceField(widget=forms.RadioSelect, label=_('Fruit Pendants'),
                                       choices=CHOICES, required=False, )
    cultivator_type = forms.ChoiceField(label=_('Cultivator Type'), choices=VALUES, widget=forms.Select())

    # batch_disfiguration = forms.ChoiceField(label="Sconfigurazione Lotto", choices=CHOICES, widget=forms.Select())
    batch_disfiguration = forms.ChoiceField(widget=forms.RadioSelect, label=_('Batch Disfiguration'),
                                            choices=CHOICES, required=False, )
    description = forms.CharField(label=_('Description'), widget=forms.Textarea, required=False,)
    social_economic_reform = forms.ChoiceField(widget=forms.RadioSelect,
                                               label=_('Social Economic reform'),
                                               choices=CHOICES, required=False, )
    urban_destination = forms.ModelChoiceField(queryset=UrbanDestination.objects.all(),
                                               label=_('Urban Destination'), required=False, )
    transformation_coefficient = forms.IntegerField(label=_('Transformation Coefficient'),
                                                    required=False, )
    IMU_final_declaration = forms.CharField(label=_('IMU Final Declaration'), required=False)
    epoch_construction = forms.CharField(label=_('Epoch Construction'), required=False, )
    building_titles = forms.CharField(label=_('Building Titles'), widget=forms.Textarea, required=False, )
    purchase_contract = forms.ChoiceField(widget=forms.RadioSelect,
                                          label=_("Purchase Contract"),
                                          choices=CHOICES, required=False, )
    constraints_other_nature = forms.CharField(label=_("Constraints Other Nature"), required=False, )
    extension_MQ = forms.FloatField(label=_("Extension MQ"), required=False,)
    residual_airspace = forms.ChoiceField(widget=forms.RadioSelect,
                                          label=_("Residual Airspace"),
                                          choices=CHOICES, required=False,)
    MC_residui = forms.CharField(label=_("MC Residui"), required=False,)
    total_demolition = forms.ChoiceField(widget=forms.RadioSelect,
                                         label=_("Total Demolition"),
                                         choices=CHOICES, required=False, )
    partial_demolition = forms.CharField(label=_("Partial Demolition"), required=False, )
    storage_state = forms.ChoiceField(widget=forms.RadioSelect,
                                      label=_("Storage State"),
                                      choices=storage_choices, required=False, )
    productive_activities = forms.ChoiceField(widget=forms.RadioSelect,
                                              label=_("Productive Activities"),
                                              choices=CHOICES, required=False, )
    lease_agreement = forms.ChoiceField(widget=forms.RadioSelect,
                                        label=_("Lease Agreement"),
                                        choices=CHOICES, required=False, )
    contract_duration = forms.FloatField(label=_("Contract Duration"), required=False, )
    contract_fee = forms.CharField(label=_("Contract Fee"), required=False)
    EBIT = forms.CharField(label=_("EBIT"), required=False, disabled=False)
    EBIt_percent = forms.CharField(label=_("EBIt %"), required=False, disabled=False)
    residual_rent = forms.CharField(label=_("Residual Rent"), required=False, )
    need_transfer_user = forms.ChoiceField(widget=forms.RadioSelect,
                                           label=_("Need Transfer User"),
                                           choices=CHOICES, required=False, )
    reclamation_activities = forms.ChoiceField(widget=forms.RadioSelect,
                                               label=_("Reclamation Activities"),
                                               choices=CHOICES, required=False, )
    reclamation_intervention_type = forms.ModelChoiceField(queryset=ReclamationInterventionType.objects.all(),
                                                           label=_("Reclamation Intervention Type"), required=False,)
    reclamation_cost = forms.CharField(label=_("Reclamation Cost"), required=False, )
    origin = forms.ChoiceField(widget=forms.Select(), label=_('Origin'),
                               choices=(
                                   ('internal', 'interno'),
                                   ('web', 'web')), initial='web', required=False, )


    def clean(self):
        """
            make fields required conditionally
        """

        data = self.cleaned_data
        registration_type = data.get('registration_type', False)
        sdc = data.get('surface_directly_concerned', False)
        oa = data.get("occupied_area", False)
        origin = data.get('origin', False)
        email = data.get('email', False)
        cls = data.get('closed', False)
        initial_value = data.get('initial_estimation_value', False)
        target_val = data.get('target_value', False)
        final_val = data.get('final_value', False)
        reven = data.get('revenue', False)
        total_cos = data.get('total_cost', False)
        turnover_marg = data.get('EBIT', False)
        closing_dat = data.get('closing_date', False)

        temporary_data = data.copy()

        # print(self.cleaned_data["EBIT"], "the ebut")
        #
        # if "," in reven:

        # self.cleaned_data["EBIT"] = str(int(reven) - int(total_cos))
        # if int(reven) - int(total_cos) == 0:
        #     print("difference is 0")
        #     print(self.cleaned_data)
        #     self.cleaned_data["EBIT"] = 0
        #     self.cleaned_data["EBIt_percent"] = 0

        if sdc and oa:
            if sdc < oa:
                self._errors['residual_surface'] = self.error_class([""])

        if origin == 'web':
            if not email:
                self._errors['email'] = self.error_class([
                    'This file is required.'])
            else:
                # get client
                customer = Customer.objects.filter(email=email)
                if not customer:
                    self._errors['email'] = self.error_class([
                        _('Please register on the site to continue with the dispute form!')])
        else:
            if cls:
                # make required
                if not initial_value:
                    self._errors['initial_estimation_value'] = self.error_class([
                        _('This file is required.')])
                if not target_val:
                    self._errors['target_value'] = self.error_class([
                        _('This file is required.')])
                if not final_val:
                    self._errors['final_value'] = self.error_class([
                        _('This file is required.')])
                if not reven:
                    self._errors['revenue'] = self.error_class([
                        _('This file is required.')])
                if not total_cos:
                    self._errors['revenue'] = self.error_class([
                        _('This file is required.')])
                if not turnover_marg:
                    self._errors['EBIT'] = self.error_class([
                        _('This file is required.')])
                if not closing_dat:
                    self._errors['closing_date'] = self.error_class([
                        _('This file is required.')])


        if registration_type == 'Esproprio Agricolo':
            # validate fields for esproprio agricolo type of reg.
            # area_type = data.get('area_type', None)
            culture_type = data.get('culture_type', None)
            fruit_pendants = data.get('fruit_pendants')
            cultivator_type = data.get('cultivator_type')
            batch_disfiguration = data.get('batch_disfiguration')
            description = data.get('description')
            # if not area_type:
            #     self._errors['area_type'] = self.error_class([
            #         'This file is required.'])
            # if not culture_type:
            #     self._errors['culture_type'] = self.error_class([
            #         _('This field is required.')])
            # if not fruit_pendants:
            #     self._errors['fruit_pendants'] = self.error_class([
            #         _('This file is required.')])
            if not cultivator_type:
                self._errors['cultivator_type'] = self.error_class([
                    _('This file is required.')])
            # if not batch_disfiguration:
            #     self._errors['batch_disfiguration'] = self.error_class([
            #         _('This file is required.')])
            # if not description:
            #     self._errors['description'] = self.error_class([
            #         _('This file is required.')])

        if registration_type in ['Esproprio Residenziale Libera', 'Esproprio Industriale Libera']:
            # validate fields for esproprio res./ind. libera type of reg.
            social_economic_reform = data.get('social_economic_reform', None)
            urban_destination = data.get('urban_destination', None)

            if not social_economic_reform:
                self._errors['social_economic_reform'] = self.error_class([
                    _('This file is required.')])
            if not urban_destination:
                self._errors['urban_destination'] = self.error_class([
                    _('This file is required.')])

        if registration_type in ['Esproprio Fabbricato Residenziale', 'Esproprio Fabbricato Industriale']:
            # validate fields for esproprio res./ind. fabbricato type of reg.
            epoch_construction = data.get('epoch_construction', None)
            building_titles = data.get('building_titles', None)
            MC_residui = data.get('MC_residui', None)
            partial_demolition = data.get('partial_demolition', None)
            total_demolition = data.get('total_demolition', None)
            residual_airspace = data.get('residual_airspace', None)
            storage_state = data.get('storage_state', None)
            lease_agreement = data.get('lease_agreement', None)
            productive_activities = data.get('productive_activities', None)
            need_transfer_user = data.get('need_transfer_user', None)
            reclamation_activities = data.get('reclamation_activities', None)
            reclamation_intervention_type = data.get('reclamation_intervention_type', None)

            if not epoch_construction:
                self._errors['epoch_construction'] = self.error_class([
                    _('This file is required.')])
            if not building_titles:
                self._errors['building_titles'] = self.error_class([
                    _('This file is required.')])
            # if not MC_residui:
            #     self._errors['MC_residui'] = self.error_class([
            #         _('This file is required.')])

            if not total_demolition:
                self.errors['total_demolition'] = self.error_class([('This file is required.')])
                if total_demolition == 'no':
                    if not partial_demolition:
                        self.errors['partial_demolition'] = self.error_class([('This file is required.')])

            if not total_demolition:
                self._errors['total_demolition'] = self.error_class([
                    _('This file is required.')])
            if not residual_airspace:
                self._errors['residual_airspace'] = self.error_class([
                    _('This file is required.')])
            if not storage_state:
                self._errors['storage_state'] = self.error_class([
                    _('This file is required.')])
            if not lease_agreement:
                self._errors['lease_agreement'] = self.error_class([
                    _('This file is required.')])
            if not productive_activities:
                self._errors['productive_activities'] = self.error_class([
                    _('This file is required.')])
            if not need_transfer_user:
                self._errors['need_transfer_user'] = self.error_class([
                    _('This file is required.')])
            if not reclamation_activities:
                self._errors['reclamation_activities'] = self.error_class([
                    _('This file is required.')])
            # if not reclamation_intervention_type:
            #     self._errors['reclamation_intervention_type'] = self.error_class([
            #         _('This file is required.')])

        return self.cleaned_data


    class Meta:
        model = Litigation
        fields = (
            'registration_type', 'dispute_matter', 'dispute_object', 'surface_directly_concerned', 'occupied_area',
            'reference', 'enrollment_amount', 'lawyer_reference', 'prejudicial_registrations',
            'origin', 'initial_estimation_value', 'target_value', 'area_address',
            'residual_surface', 'culture_type', 'above_ground_quantification', 'fruit_pendants',
            'cultivator_type', 'batch_disfiguration', 'description', 'reception_act', 'purchase_contract',
            'contract_date', 'social_economic_reform', 'urban_destination', 'transformation_coefficient',
            'IMU_final_declaration', 'epoch_construction', 'building_titles', 'extension_MQ', 'MC_residui',
            'partial_demolition', 'total_demolition', 'residual_airspace', 'storage_state', 'lease_agreement',
            'productive_activities', 'contract_duration', 'contract_fee', 'residual_rent', 'need_transfer_user',
            'reclamation_activities', 'reclamation_intervention_type', 'reclamation_cost', 'reception_act',
            'purchase_contract', 'date_receipt_act', 'contract_date', 'technical_reference', 'last_notary_fees',
            'constraints_other_nature', 'other_constraints_type', 'urban_destination',
            # 'starting_data', 'target_data', 'closing_data'
        )

    layout = Layout(
        Fieldset(_('Litigation Form')),
        Fieldset(
            None,
            Row('dispute_matter', 'dispute_object'),
            Row('initial_estimation_value', 'target_value'),
        ),
        Fieldset(
            None,
            Row('origin')
        ),
        Fieldset(_('Registration'),
                 Row('registration_type', 'prejudicial_registrations'),
                 Row('enrollment_amount'),
                 ),
        Fieldset(_('Reference'),
                 Row('lawyer_reference', 'reference'),
                 ),
        Fieldset(_('Area'),
                 Row('surface_directly_concerned', 'occupied_area', 'residual_surface'),
                 Row('area_address'),  # 'occupied_area'
                 ),
        Fieldset(_('Edificio'), # edificio agricultural-expropriation
                 Row('culture_type'),  # 'area_type',
                 Row('above_ground_quantification'),
                 Row('fruit_pendants', 'cultivator_type', 'batch_disfiguration'),
                 Row('description'),
                 ),
        Fieldset('',
                 Row('social_economic_reform', 'urban_destination'),
                 Row('transformation_coefficient', 'IMU_final_declaration'),
                 ),
        Fieldset('',
                 Row('epoch_construction', 'building_titles'),
                 Row('extension_MQ', 'MC_residui'),
                 Row('total_demolition', 'partial_demolition', 'residual_airspace', 'storage_state', ),
                 Row('lease_agreement', 'productive_activities'),
                 Row('contract_duration', 'contract_fee', 'residual_rent'),
                 Row('need_transfer_user', 'reclamation_activities', 'reclamation_intervention_type'),
                 Row('reclamation_cost'),
                 ),

        Fieldset(
            None,
            Row('reception_act', 'date_receipt_act', ),
            Row('purchase_contract', 'contract_date'),
        ),
        Fieldset(_('contact-information'),
                 Row('email', ),
                 ),
    )

