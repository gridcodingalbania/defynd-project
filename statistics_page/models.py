# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Statistics(models.Model):

    @property
    def initial__value(self):
        return str(self.initial_value) + " €" if str(self.initial_value) else ""

    @property
    def objective__value(self):
        return str(self.objective_value) + " €" if str(self.objective_value) else ""

    @property
    def final__value(self):
        return str(self.final_value) + " €" if str(self.final_value) else ""

    @property
    def revue__value(self):
        return str(self.revue_value) + " €" if str(self.revue_value) else ""

    @property
    def total__value(self):
        return str(self.total_value) + " %" if str(self.total_value) else ""

    @property
    def revue__value(self):
        return str(self.revue_value) + " €" if str(self.revue_value) else ""

    @property
    def total__cost_value(self):
        return str(self.total_cost_value) + " €" if str(self.total_cost_value) else ""

    @property
    def margin__value(self):
        return str(self.margin_value) + " €" if str(self.margin_value) else ""


    title = models.CharField(_("Title"), max_length=100, null=True, blank=True)
    number = models.IntegerField(_("Number"), null=True, blank=True)
    initial_value = models.FloatField(_("Initial Value"), null=True, blank=True)
    objective_value = models.FloatField(_("Objective Value"), null=True, blank=True)
    final_value = models.FloatField(_("Final Value"), null=True, blank=True)
    total_value = models.FloatField(_("Total Value"), null=True, blank=True)

    revue_value = models.FloatField(_("Revue Value"), null=True, blank=True)
    total_cost_value = models.FloatField(_("Total Cost"), null=True, blank=True)
    margin_value = models.FloatField(_("Margin Value"), null=True, blank=True)


    class Meta:
        verbose_name = _('statistic')
        verbose_name_plural = _('statistics')