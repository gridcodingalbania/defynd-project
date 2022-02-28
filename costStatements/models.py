from django.db import models
from clients import models as customer
from litigations import models as litigation
from django.utils.translation import gettext_lazy as _
import logging

_logger = logging.getLogger(__name__)


def increment_costStatement_number():
    """ Increment cost statement code  
    """
    prefix = 'CST'
    code = prefix + '001'
    last_statement = CostStatement.objects.all().order_by('id').last()
    if not last_statement:
        return code
    last_code = last_statement.name
    sequence = int(last_code[3:]) + 1
    code = prefix + str(sequence).zfill(3)
    return code


class ItemCategory(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    code = models.CharField(_("Code"), max_length=8, null=True,
                            help_text=_("Code Change Message"))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return "%s" % self.name


class Item(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    code = models.CharField(_("Code"), max_length=100, null=True)
    priority = models.IntegerField(_("Priority"), null=True, blank=True)
    category = models.ForeignKey(ItemCategory, verbose_name=_("category"),
                                 on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "item"
        ordering = ['priority']
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        constraints = [
            models.UniqueConstraint(fields=['code'], name='unique_code')
        ]


class CostStatement(models.Model):
    name = models.CharField(_("name"), max_length=100, null=True, default=increment_costStatement_number)
    code = models.CharField(_("code"), max_length=20, null=True)
    client = models.ForeignKey(customer.Customer,
                               verbose_name=_("Client"),
                               on_delete=models.CASCADE, null=True)
    litigation = models.ForeignKey(litigation.Litigation,
                                   verbose_name=_("Litigation"),
                                   on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(_("Created Date"), auto_now_add=True, db_index=True,
                                blank=True, null=True)
    init_amount = models.FloatField(_("Init Amount"), blank=True, null=True)
    total = models.FloatField(_("Total Cost"), blank=True, null=True)
    url = models.FloatField(_("Url"), blank=True, null=True)
    init_negotiation = models.IntegerField(_("Init Negotiation"), null=True, )
    expected_dealing_term = models.IntegerField(_("Expected dealing Term"), null=True, )

    def __str__(self):
        return "[%s] %s" % (self.code, self.name)

    class Meta:
        db_table = "cost_statement"
        verbose_name = _('cost Statement')
        verbose_name_plural = _('Cost Statements')


class Hypothesis(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    description = models.CharField(_("Description"), max_length=256, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "hypothesis"
        verbose_name = _('Hypothesis')
        verbose_name_plural = _('hypothesis Plural')


class CostStatementItem(models.Model):
    item = models.ForeignKey(Item, verbose_name=_("Item"),
                             on_delete=models.CASCADE, null=True)
    cost_statement = models.ForeignKey(CostStatement, verbose_name=_("Cost Statement"),
                                       on_delete=models.CASCADE, null=True)
    value = models.FloatField(verbose_name=_("Value"), blank=True, null=True)
    hypothesis = models.ForeignKey(Hypothesis, verbose_name=_("Hypothesis"),
                                   on_delete=models.CASCADE, null=True, blank=True, )
    percentage = models.FloatField(verbose_name="%", blank=True, null=True)
    time = models.DateTimeField(_("Created Date"), auto_now_add=True, db_index=True,
                                blank=True, null=True)

    def __str__(self):
        return "%s" % self.item.name

    class Meta:
        db_table = "cost_statement_item"
        verbose_name = _('Cost Statement Item')
        verbose_name_plural = _('Cost Statement Items')



