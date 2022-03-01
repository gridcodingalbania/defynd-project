from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StatisticsPageConfig(AppConfig):
    name = 'statistics_page'
    verbose_name = _('Dashboard_page')