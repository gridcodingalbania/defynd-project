from django.contrib import admin
from .models import Customer
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _


class CustomerAdmin(admin.ModelAdmin):
    # menu_title = "Clients"
    list_display = (
        'code',
        'customer_type',
        'vat_number',
        'company_name',
        'name',
        'email',
        'phone',
        'mobile',
        'origin',
        'is_active',
    )
    search_fields = ('code', 'first_name', 'last_name', 'company_name',
                     'email', 'phone', 'mobile', 'birthday', 'fiscal_code', 'vat_number')
    list_filter = ('customer_type', 'company_name', 'gender', 'birthplace', 'is_customer', 'is_active', 'vat_number')
    fieldsets = [
        (
            None,
            {
                'fields': ('code', 'customer_type')
            }
        ),
        (
            None,
            {
                'fields': ('company_name', 'contact_person', 'role')
            }
        ),
        (
            None,
            {
                'fields': ('first_name', 'last_name'),
                'classes': ('wide', 'extrapretty', 'individual')
            }
        ),
        (
            _('personal-info'),
            {
                'fields': ('fiscal_code', 'vat_number', 'birthplace', 'birthday', 'gender'),
                'classes': ('wide', 'extrapretty', 'individual')
            }
        ),
        (
            _('contact-info'),
            {
                'fields': ('email', 'phone', 'mobile')
            }
        ),
        (
            _('address'),
            {
                'fields': ('street', 'city', 'post_number',)
            }
        ),
        (
            None,
            {
                'fields': ('is_customer',)
            }
        )
    ]

    form = ContactForm

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
            'admin/js/contact_type.js',  # project static folder
        )


admin.site.register(Customer, CustomerAdmin)
