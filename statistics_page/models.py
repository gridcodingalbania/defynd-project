# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Statistics(models.Model):
    name = models.CharField(_("Name"), max_length=100, null=True, blank=True)
    initial_value = models.FloatField(_("Initial Value"), null=True, blank=True)
    objective_value = models.FloatField(_("Objective Value"), null=True, blank=True)
    final_value = models.FloatField(_("Final Value"), null=True, blank=True)
    total_value = models.FloatField(_("Total Value"), null=True, blank=True)

    revue_value = models.FloatField(_("Revue Value"), null=True, blank=True)
    total_cost_value = models.FloatField(_("Total Cost"), null=True, blank=True)
    margin_value = models.FloatField(_("Margin Value"), null=True, blank=True)
    description = models.CharField(_("Description"), max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = _('statistic')
        verbose_name_plural = _('statistics')