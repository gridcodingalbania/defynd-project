from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContractsConfig(AppConfig):
    name = 'contracts'
    verbose_name = _('contracts-app')
