from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StatisticsPageConfig(AppConfig):
    name = 'statistics_page'
    verbose_name = _('dashboard_page')
