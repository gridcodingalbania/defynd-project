from django.db import models
from django.utils.translation import gettext_lazy as _


def add_commas(value):
    input = str(value).split(".")[0]
    if len(input) <= 3:
        return str(value)
    else:
        response = ""
        for char in input[::-1]:
            response = char + response
            if len("".join(response.split(","))) % 3 == 0:
                response = "," + response
        if response[0] == ",":
            response = response[1:]
        return response

# Create your models here.
class Statistics(models.Model):

    @property
    def initial__value(self):
        return add_commas(self.initial_value) + " €" if add_commas(self.initial_value) else ""

    @property
    def objective__value(self):
        return add_commas(self.objective_value) + " €" if add_commas(self.objective_value) else ""

    @property
    def final__value(self):
        return add_commas(self.final_value) + " €" if add_commas(self.final_value) else ""

    @property
    def revue__value(self):
        return add_commas(self.revue_value) + " €" if add_commas(self.revue_value) else ""

    @property
    def total__value(self):
        return add_commas(self.total_value) + " %" if add_commas(self.total_value) else ""

    @property
    def revue__value(self):
        return add_commas(self.revue_value) + " €" if add_commas(self.revue_value) else ""

    @property
    def total__cost_value(self):
        return add_commas(self.total_cost_value) + " €" if add_commas(self.total_cost_value) else ""

    @property
    def ebit__(self):
        return add_commas(self.ebit) + " €" if add_commas(self.ebit) else ""

    @property
    def ebit__percent(self):
        return add_commas(self.ebit_percent) + " %" if add_commas(self.ebit_percent) else ""

    title = models.CharField(_("Title"), max_length=100, null=True, blank=True)
    number = models.IntegerField(_("Number"), null=True, blank=True)
    initial_value = models.FloatField(_("Initial Value"), null=True, blank=True)
    objective_value = models.FloatField(_("Objective Value"), null=True, blank=True)
    final_value = models.FloatField(_("Final Value"), null=True, blank=True)
    total_value = models.FloatField(_("Total Value"), null=True, blank=True)

    revue_value = models.FloatField(_("Revue Value"), null=True, blank=True)
    total_cost_value = models.FloatField(_("Total Cost"), null=True, blank=True)
    ebit = models.FloatField(_("ebit"), null=True, blank=True)
    ebit_percent = models.FloatField(_("ebit_percent"), null=True, blank=True)


    class Meta:
        verbose_name = _('statistic')
        verbose_name_plural = _('statistics')