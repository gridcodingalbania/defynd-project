from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientsConfig(AppConfig):
    name = 'clients'
    verbose_name = _('clients')
