from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Statistics(models.Model):
    name = models.CharField(_("Name"), max_length=100, null=True)
    initial_value = models.IntegerField(_("Initial Value"), null=True)
    objective_value = models.IntegerField(_("Objective Value"), null=True)
    final_value = models.IntegerField(_("Final Value"), null=True)
    total_value = models.IntegerField(_("Total Value"), null=True)

    revue_value = models.IntegerField(_("Revue Value"), null=True)
    total_cost_value = models.IntegerField(_("Total Cost"), null=True)
    margin_value = models.IntegerField(_("Margin Value"), null=True)
    description = models.CharField(_("Description"), max_length=100, null=True)
