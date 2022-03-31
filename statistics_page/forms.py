from django import forms
from django.utils.translation import gettext_lazy as _


# Registration FORM
class StatisticsForm(forms.ModelForm):
    total_value = forms.FloatField(label=_("Moltiplicatore"), required=False)
