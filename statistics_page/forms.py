from django import forms
from django.utils.translation import gettext_lazy as _


# Registration FORM
class StatisticsForm(forms.ModelForm):
    total_value = forms.FloatField(label=_("Moltiplicatore"), required=False)
    title = forms.CharField(_("Title"), max_length=100, null=True, blank=True)
    number = forms.IntegerField(_("Number"), null=True, blank=True)
    initial_value = forms.FloatField(_("Initial Value"), null=True, blank=True)
    objective_value = forms.FloatField(_("Objective Value"), null=True, blank=True)
    final_value = forms.FloatField(_("Final Value"), null=True, blank=True)
    revue_value = forms.FloatField(_("Revue Value"), null=True, blank=True)
    total_cost_value = forms.FloatField(_("Total Cost Value"), null=True, blank=True)
    ebit = forms.FloatField(_("Ebit"), null=True, blank=True)
    ebit_percent = forms.FloatField(_("Ebit Percent"), null=True, blank=True)