from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LitigationsConfig(AppConfig):
    name = 'litigations'
    verbose_name = _('Litigation App')