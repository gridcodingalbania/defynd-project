from django.db import models
from django.conf import settings
from clients import models as customer
from lawyers import models as lawyer
from configurations import models as config
from django.utils.translation import gettext_lazy as _
import datetime


def increment_litigation_number():
    """ Increment litigation (case) code  
    """
    year = datetime.date.today().year
    prefix = str(year)
    code = prefix + '0001'
    last_litigation = Litigation.objects.all().order_by('id').last()
    if not last_litigation:
        return code
    last_code = last_litigation.name
    sequence = int(last_code[4:]) + 1
    code = prefix + str(sequence).zfill(4)
    return code


class Litigation(models.Model):
    CHOICES = (
        (None, ''),
        ('Esproprio Agricolo', 'Agricultural expropriation'),
        ('Esproprio Residenziale Libera', 'Esproprio Residenziale Libera'),
        ('Esproprio Industriale Libera', 'Esproprio Industriale Libera'),
        ('Esproprio Fabbricato Residenziale', 'Esproprio Fabbricato Residenziale'),
        ('Esproprio Fabbricato Industriale', 'Esproprio Fabbricato Industriale'),
    )

    choices = [
        ('yes', 'si'),
        ('no', 'no'),
    ]

    values = [
        ('value_1', 'value-1'),
        ('value_2', 'value-2'),
    ]


    name = models.CharField(_("litigation-code"), max_length=20, unique=True,
                            default=increment_litigation_number, )

    # closed = models.BooleanField(_("closed"), default=True)

    client = models.ForeignKey(customer.Customer,
                               verbose_name=_("client"),
                               on_delete=models.CASCADE, blank=True, null=True)
    hyperlink = models.URLField(verbose_name=_("HyperLink to Economics Sheet"), blank=True, null=True, max_length=7000)
    upload_pdf = models.FileField(_("Upload File"), upload_to='documents/')
    # contract = models.
    dispute_matter = models.ForeignKey(config.DisputeMatter,
                                       verbose_name=_("Controversy Matter"), on_delete=models.CASCADE, null=True)
    dispute_object = models.ForeignKey(config.DisputeObject,
                                       verbose_name=_("Dispute Object"), on_delete=models.CASCADE, null=True)
    starting_date = models.DateField(_("Starting Date"), max_length=100, null=True)
    target_date = models.DateField(_("Target Data"), max_length=100, null=True)
    closing_date = models.DateField(_("Closing Date"), max_length=100, null=True, blank=True)
    initial_estimation_value = models.DecimalField(_("Initial Estimation Value"),
                                                   max_digits=32, decimal_places=2,
                                                   default=0, blank=True, null=True)  # currency
    target_value = models.DecimalField(_("Target Value"),
                                       max_digits=32, decimal_places=2,
                                       default=0, blank=True, null=True)  # currency
    final_value = models.DecimalField(_("Final Value"),
                                      max_digits=50, decimal_places=2,
                                      default=0, blank=True, null=True)


    revenue = models.IntegerField(_("Revenue"), blank=True, null=True)
    total_cost = models.IntegerField(_("Total Cost"), blank=True, null=True)
    turnover_margin = models.IntegerField(_("Turnover Margin"), blank=True, null=True)


    reference = models.CharField(_("Reference"), max_length=100, blank=True, null=True)
    prejudicial_registrations = models.CharField(_("Prejudicial Registrations"),
                                                 max_length=100, blank=True, null=True)
    registration_type = models.CharField(_("Registration Typology"),
                                         max_length=100,
                                         choices=CHOICES,
                                         default=None,
                                         null=True)
    enrollment_amount = models.DecimalField(_("Enrollment Amount"),
                                            max_digits=32, decimal_places=2,
                                            default=0, blank=True, null=True)  # currency
    surface_directly_concerned = models.FloatField(_("Surface Directly Concerned"),
                                                   blank=True, null=True)
    residual_surface = models.FloatField(_("Residual Surface"),
                                         blank=True, null=True)
    technical_reference = models.CharField(_("Technical Reference"), max_length=100,
                                           blank=True, null=True)
    lawyer_reference = models.ForeignKey(lawyer.Lawyer,
                                         verbose_name=_("Lawyer Reference"),
                                         on_delete=models.CASCADE, blank=True, null=True)
    area_address = models.CharField(_("Area Address"), max_length=100, blank=True, null=True)
    occupied_area = models.FloatField(_("Occupied Area"), max_length=100, blank=True, null=True)
    reception_act = models.CharField(_("Reception Area"),
                                     max_length=100,
                                     choices=choices,
                                     default='no',
                                     blank=True,
                                     null=True)
    date_receipt_act = models.DateField(_("Date Receipt Act"), blank=True, null=True)
    last_notary_fees = models.DecimalField(_("Last Notary Fees"),
                                           max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    other_constraints_type = models.ForeignKey(config.ConstraintType,
                                               verbose_name=_("Other Constraints Type"),
                                               on_delete=models.CASCADE, blank=True, null=True)

    # TODO: default value from the logged user registering the form
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_("User"), blank=True, null=True,
                             default=1, on_delete=models.CASCADE)
    # area_type = models.ForeignKey(config.AreaType,
    #     verbose_name="Tipologia Area",
    #     on_delete=models.CASCADE, blank=True, null=True)
    culture_type = models.ForeignKey(config.CultureType,
                                     verbose_name=_("Culture Type"),
                                     on_delete=models.CASCADE, blank=True, null=True)
    fruit_pendants = models.CharField(_("Fruit Pendants"),
                                      max_length=100,
                                      choices=choices,
                                      default='no',
                                      blank=True,
                                      null=True)
    cultivator_type = models.CharField(_("Cultivator Type"),
                                       max_length=100,
                                       choices=values,
                                       default='no',
                                       blank=True,
                                       null=True)
    above_ground_quantification = models.IntegerField(_("Above Ground Quantification"),
                                                     help_text=_("Plant Name"),
                                                     blank=True, null=True, default=0)
    batch_disfiguration = models.CharField(_("Batch Disfiguration"),
                                           max_length=100,
                                           choices=choices,
                                           default='no',
                                           blank=True,
                                           null=True)

    description = models.TextField(_("Description"), blank=True, null=True)
    social_economic_reform = models.CharField(_("Social Economic Reform"),
                                              max_length=100,
                                              choices=choices,
                                              default='no',
                                              blank=True,
                                              null=True)
    urban_destination = models.ForeignKey(config.UrbanDestination,
                                          verbose_name=_("Urban Destination"),
                                          on_delete=models.CASCADE, blank=True, null=True)
    transformation_coefficient = models.IntegerField(_("Transformation Coefficient"),
                                                     blank=True, null=True, default=0)
    IMU_final_declaration = models.DecimalField(_("Fianl Declaration IMU"),
                                                max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    epoch_construction = models.DecimalField(_("Epoch Constrution"),
                                             max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    building_titles = models.TextField(_("Building Titles"), blank=True, null=True)
    contract_date = models.DateField(_("Contract Date"), blank=True, null=True)
    last_notary_fees = models.DecimalField(_("Last Notary Fees"),
                                           max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    constraints_other_nature = models.CharField(_("Constraints Other Nture"),
                                                max_length=100, blank=True, null=True)
    extension_MQ = models.FloatField(_("Eextension MQ"), blank=True, null=True,
                                     default=0.0)
    # TODO: check contratto d'acquisto -- link with contract module/entity
    purchase_contract = models.CharField(_("Purchase Constract"),
                                         max_length=100,
                                         choices=choices,
                                         default='no',
                                         blank=True,
                                         null=True)
    residual_airspace = models.CharField(_("Residual Airspace"),
                                         max_length=100,
                                         choices=choices,
                                         default='no',
                                         blank=True,
                                         null=True)
    MC_residui = models.CharField(_("MC Residui"),
                                  max_length=100, blank=True, null=True)
    total_demolition = models.CharField(_("Total Demolition"),
                                        max_length=100,
                                        choices=choices,
                                        default='no',
                                        blank=True,
                                        null=True)
    partial_demolition = models.CharField(_("Partial Demolition"),
                                          max_length=100, blank=True, null=True)
    storage_state = models.CharField(_("Storage State"),
                                     max_length=100,
                                     choices=[
                                         ('great', 'ottimo'),
                                         ('good', 'buono'),
                                         ('enough', 'sufficiente'),
                                         ('to_be_restructured', 'da ristrutturare'),
                                     ],
                                     blank=True,
                                     null=True)
    productive_activities = models.CharField(_("Productive Activities"),
                                             max_length=100,
                                             choices=choices,
                                             default='no',
                                             blank=True,
                                             null=True)
    lease_agreement = models.CharField(_("Lease Agreement"),
                                       max_length=100,
                                       choices=choices,
                                       default='no',
                                       blank=True,
                                       null=True)
    contract_duration = models.FloatField(_("Contract Duration"),
                                          blank=True, null=True, default=0)
    contract_fee = models.DecimalField(_("Contract fee"), default=0,
                                       max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    residual_rent = models.DecimalField(_("Residual Rent"), default=0,
                                        max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    need_transfer_user = models.CharField(_("Nees Transfer User"),
                                          max_length=100,
                                          choices=choices,
                                          default='no',
                                          blank=True,
                                          null=True)
    reclamation_activities = models.CharField(_("Reclamation Activities"),
                                              max_length=100,
                                              choices=choices,
                                              default='no',
                                              blank=True,
                                              null=True)
    reclamation_intervention_type = models.ForeignKey(config.ReclamationInterventionType,
                                                      verbose_name=_("Reclamation Intervention Type"),
                                                      on_delete=models.CASCADE, blank=True, null=True)
    reclamation_cost = models.DecimalField(_("Reclamation Cost"), default=0.0,
                                           max_digits=32, decimal_places=2, blank=True, null=True)  # currency
    time = models.DateTimeField(_("Date"), auto_now_add=True, db_index=True,
                                blank=True, null=True)
    # if it is concluded with high ranking and associated with cost statement & contract
    closed = models.BooleanField(_("Closed"), default=False)
    origin = models.CharField(_("Origin"), choices=(
        ('internal', 'interno'),
        ('web', 'web')), max_length=8, default='internal', blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)


    class Meta:
        db_table = "litigation"
        ordering = ['name']
        verbose_name = _('litigation')
        verbose_name_plural = _('litigations')
