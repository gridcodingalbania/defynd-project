from django.db import models
from django.utils.translation import gettext_lazy as _

phone_prefixes = (
    ('+39', '+39'),
    ('+355', '+355'),
    ('+44', '+44'),
    ('+43', '+43'),
    ('+32', '+32'),
    ('+359', '+359'),
    ('+357', '+357'),
    ('+420', '+420'),
    ('+45', '+45'),
    ('+372', '+372'),
    ('+358', '+358'),
    ('+33', '+33'),
    ('+49', '+49'),
    ('+49', '+49'),
    ('+30', '+30'),
    ('+36', '+36'),
    ('+354', '+354'),
    ('+353', '+353'),
    ('+371', '+371'),
    ('+423', '+423'),
    ('+370', '+370'),
    ('+352', '+352'),
    ('+356', '+356'),
    ('+31', '+31'),
    ('+47', '+47'),
    ('+48', '+48'),
    ('+351', '+351'),
    ('+40', '+40'),
    ('+421', '+421'),
    ('+421', '+421'),
    ('+386', '+386'),
    ('+34', '+34'),
    ('+46', '+46'),
    ('+383', '+383'),
    ('+389', '+389'),
    ('+382', '+382'),
    ('+381', '+381'),
    ('+381', '+381'),
    ('+41', '+41'),
    ('+90', '+90'),
    ('+380', '+380'),
)

def increment_customer_number():
    code = 'C' + '001'
    last_contact = Customer.objects.all().order_by('id').last()
    if not last_contact:
        return code
    last_code = last_contact.code
    sequence = int(last_code[1:]) + 1
    code = 'C' + str(sequence).zfill(3)
    return code


class Customer(models.Model):
    code = models.CharField(_("Code"), max_length=20, unique=True,
                            default=increment_customer_number, )  # editable=False
    hubspot_card = models.URLField(verbose_name=_("Hubspot Card"), blank=True, null=True, max_length=7000)
    # fill name from company_name if company or name surname if individual
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)

    fiscal_code = models.CharField(_("Fiscal Code"), max_length=100, blank=True, null=True)
    vat_number = models.CharField(_("Vat Number"), max_length=100, blank=True, null=True)

    company_name = models.CharField(_("Company Name"), max_length=100, blank=True, null=True)
    # TODO: possibility to add more than one contacts per company - contacts field m2m below
    contact_person = models.CharField(_("Contact Person"), max_length=100, blank=True, null=True)
    role = models.CharField(_("Role"), max_length=100, blank=True, null=True)

    first_name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=True, null=True)

    email = models.EmailField(_("e-mail"), null=True, unique=True, )
    phone_prefix = models.CharField(max_length=100,
                                    choices=phone_prefixes,
                                    default=None,
                                    null=True)
    phone = models.IntegerField(_("Phone"), blank=True, null=True)
    mobile_prefix = models.CharField(max_length=100,
                                    choices=phone_prefixes,
                                    default=None,
                                    null=True)
    mobile = models.IntegerField(_("Mobile"), blank=True, null=True)
    gender = models.CharField(_("Gender"),
                              choices=((None, ''),
                                       ('F', 'Femmina'),
                                       ('M', 'Maschio')), max_length=10, default=None, blank=True, null=True)
    birthday = models.DateField(_("Birthday"), null=True, blank=True)
    birthplace = models.CharField(_("Birth-place"), max_length=100, blank=True, null=True)

    street = models.CharField(_("Street"), max_length=256, null=True, )
    # TODO: city: add entity? If so, should be preconfigured for public usage
    city = models.CharField(_("City"), max_length=256, null=True, )
    post_number = models.CharField(_("Post Number"), max_length=100, null=True)

    customer_type = models.CharField(_("Customer Type"),
                                     choices=(('individual', 'Individuo'),
                                              ('company', 'Azienda'),), max_length=16, default='individual', null=True)
    contacts = models.ManyToManyField('self', verbose_name=_('contacts'), blank=True, )
    is_customer = models.BooleanField(_("Is Customer"), db_index=True, default=False, )
    is_active = models.BooleanField(_("Is Active"), db_index=True, default=False, )
    origin = models.CharField(_("origin"), choices=(
        ('internal', 'interno'),
        ('web', 'web')), max_length=8, default='internal', blank=True, null=True)

    def __str__(self):
        return "[%s] %s" % (self.code, self.name)

    def __init__(self, *args, **kwargs):
        # TODO: filter to show only individuals in m2m contacts field
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """ activate by default if contact is registered interally
        """
        if self.origin == 'internal':
            self.is_active = True
        super(Customer, self).save(*args, **kwargs)

    @property
    def name(self):
        name = self.company_name
        if self.customer_type == 'individual':
            name = ''.join([self.first_name or " ", ' ', self.last_name or " "])
        return name

    class Meta:
        db_table = "customer"
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
