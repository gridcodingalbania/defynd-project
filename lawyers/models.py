from django.db import models
from django.utils.translation import gettext_lazy as _


class Lawyer(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "lawyer"
        verbose_name = _('Lawyer')
        verbose_name_plural = _('Lawyers')
