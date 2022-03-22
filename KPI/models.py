from django.db import models
from statistics_page import utils
# Create your models here.


class KPI(models.Model):
    contenziosi_in_gestione = models.CharField(max_length=200, null=True, blank=True)