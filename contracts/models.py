from django.db import models
from django.utils import timezone
from costStatements import models as statement
from clients import models as customer
from django.utils.translation import gettext_lazy as _


def increment_contract_number():
    """ Increment contract code  
    """
    prefix = 'CR'
    code = prefix + '001'
    last_contract = Contract.objects.all().order_by('id')
    if not last_contract:
        return code
    last_code = last_contract.last().code
    sequence = int(last_code[3:]) + 1
    code = prefix + str(sequence).zfill(3)
    return code


class Contract(models.Model):
    code = models.CharField(_("Code"), max_length=100, null=True,
            default=increment_contract_number) 
    name = models.CharField(_("Name"), max_length=100, null=True, blank=True,)
    date = models.DateField(_("Date"), null=True, blank=True, default=timezone.now)
    sign_date = models.DateField(_("Sign Date"), null=True, blank=True)
    client = models.ForeignKey(customer.Customer, verbose_name=_("Client"), on_delete=models.CASCADE, null=True)
    # statement = models.ForeignKey(statement.CostStatement, verbose_name=_("Cost Statement"), on_delete=models.CASCADE, null=True)
    url = models.FloatField(_("Url"), blank=True, null=True)

    class Meta:
        db_table = "contract"
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')
    
    def __str__(self):
        return self.code
