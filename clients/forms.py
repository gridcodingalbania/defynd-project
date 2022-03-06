from django import forms
from material import Layout, Row, Fieldset, Span2, Span3
from .models import Customer
from django.utils.translation import gettext_lazy as _


CHOICES = (
    ('F', _('female')),
    ('M', _('male'))
)

contact_choices = (
    ('individual', _('individual')),
    ('company', _('company')),
)

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


# Registration FORM
class ContactForm(forms.ModelForm):

    vat_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-uppercase'}), required=False)
    fiscal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-uppercase'}), required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect, label=_('Gender'), choices=CHOICES,
                               required=False)
    birthday = forms.DateField(
        widget=forms.DateInput(),
        input_formats=('%d/%m/%Y',),  # '%dd-%mm-%YYYY', '%Y-%m-%d'
        help_text="d/mm/yyyy",
        label=_('Birthday'),
        required=False
    )
    phone_prefix = forms.ChoiceField(widget=forms.Select(), choices=phone_prefixes, label=_('Phone'))
    mobile_prefix = forms.ChoiceField(widget=forms.Select(), choices=phone_prefixes, label=_('Mobile'))
    phone = forms.IntegerField(label="")
    mobile = forms.IntegerField(label="")
    customer_type = forms.ChoiceField(widget=forms.Select(), label=_('Customer Type'),
                                      choices=contact_choices, required=True, )
    origin = forms.ChoiceField(widget=forms.Select(), label=_('Origin'),
                               choices=(
                                   ('internal', 'interno'),
                                   ('web', 'web')), initial='web', required=False, )

    agree_toc = forms.BooleanField(label=_("Agree"),
                                   help_text=_("Agree Condition"), required=False)
    # TODO: additional labels will be updated once client sends the description
    agree_toc_1 = forms.BooleanField(label=_("Agree"),
                                     help_text=_("Agree Contact"), required=False)
    agree_toc_2 = forms.BooleanField(label=_("Agree"), required=False)
    agree_toc_3 = forms.BooleanField(label=_("Agree"), required=False)

    def clean(self):
        """
            make fields required conditionally
        """
        data = self.cleaned_data
        code = data.get('code', False)
        customer_type = data.get('customer_type', False)
        agree_toc = data.get('agree_toc', False)
        agree_toc_1 = data.get('agree_toc_1', False)
        agree_toc_2 = data.get('agree_toc_2', False)
        agree_toc_3 = data.get('agree_toc_3', False)
        email = data.get('email', False)
        if email:
            try:
                if code:
                    print("edit mode", code)
                    saved_customer = Customer.objects.get(code=code)
                    db_email = saved_customer.email
                    if db_email != email:
                        Customer.objects.get(email=email)
                        self._errors['email'] = self.error_class(_('Email already exists.'))

                else:
                    # if no error is caught then the customer is in the db --> warn user for duplicate email
                    Customer.objects.get(email=email)
                    self._errors['email'] = self.error_class(_('Email already exists.'))

            except Customer.DoesNotExist:
                print(_("No duplicate customer found for this email, proceeding to save in db."))

        # origin added as hidden in form in order to have a value in response
        origin = data.get('origin', None)

        # make required only in form registration
        print(origin)
        if origin == 'web':
            if not agree_toc:
                self._errors['agree_toc'] = self.error_class([_('Required Field')])
            if not agree_toc_1:
                self._errors['agree_toc_1'] = self.error_class([_('Required Field')])
            if not agree_toc_2:
                self._errors['agree_toc_2'] = self.error_class([_('Required Field')])
            if not agree_toc_3:
                self._errors['agree_toc_3'] = self.error_class([_('Required Field')])

        if customer_type == 'individual':
            # validate fields for individual type of reg.
            first_name = data.get('first_name', None)
            last_name = data.get('last_name', None)
            birthday = data.get('birthday', None)
            phone = data.get('phone', None)

            if not first_name:
                self._errors['first_name'] = self.error_class([_('Required Field')])
            if not last_name:
                self._errors['last_name'] = self.error_class([_('Required Field')])
            if not birthday:
                self._errors['birthday'] = self.error_class([_('Required Field')])
            if not phone:
                self._errors['phone'] = self.error_class([_('Required Field')])
            # if not fiscal_code:
            #     self._errors['fiscal_code'] = self.error_class([
            #         'Questo campo è obbligatorio.'])

        if customer_type == 'company':
            # validate fields for individual type of reg.
            company_name = data.get('company_name', None)
            fiscal_code = data.get('fiscal_code', None)
            vat_number = data.get('vat_number', None)
            role = data.get('role', None)

            if not company_name:
                self._errors['company_name'] = self.error_class([_('Required Field')])
            if not fiscal_code:
                self._errors['fiscal_code'] = self.error_class([_('Required Field')])
            if not vat_number:
                self._errors['vat_number'] = self.error_class([_('Required Field')])
            if not role:
                self._errors['role'] = self.error_class([_('Required Field')])
        return self.cleaned_data

    class Meta:
        model = Customer
        fields = ('birthday', 'birthplace',
                  'fiscal_code', 'vat_number', 'gender', 'email', 'phone',
                  'company_name', 'first_name', 'last_name',
                  'contact_person', 'role',
                  'mobile', 'street', 'city', 'post_number',
                  'customer_type', 'contacts', 'origin'
                  )

    layout = Layout(
        Fieldset(_('Registration')),
        Fieldset(
            None,
            Row('customer_type', )
        ),
        Fieldset(
            None,
            Row('origin',),
        ),
        Fieldset(
            None,
            Row('company_name'),
            Row('fiscal_code', 'vat_number')
        ),
        Fieldset(
            None,
            Row('first_name', 'last_name', ),
        ),
        Fieldset(
            None,
            Row('role'),  # 'contact_person',
            Row(Span2('email'), 'phone_prefix', 'phone', 'mobile_prefix','mobile', ),
            Row('birthplace', 'birthday'),
            Row('gender', ),
        ),
        Fieldset(
            _('Address'),
            Row(Span3('street'), 'city', 'post_number', ),
        ),
        Fieldset(
            None,
            Row(Span2('agree_toc'), ),
            Row(Span2('agree_toc_1'), ),
            Row(Span2('agree_toc_2'), ),
            Row(Span2('agree_toc_3'), ),
        ),
    )
