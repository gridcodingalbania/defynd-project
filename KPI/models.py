from django.db import models

# Create your models here.


class KPI(models.Model):
    contenziosi_in_gestione = models.CharField(max_length=200, null=True, blank=True)
    contenziosi_definiti = models.CharField(max_length=200, null=True, blank=True)
    contenziosi_aperti = models.CharField(max_length=200, null=True, blank=True)
    contenziosi_trattativa = models.CharField(max_length=200, null=True, blank=True)

    valore_iniziale_totale = models.FloatField(null=True, blank=True)
    valore_obiettivo_totale = models.FloatField(null=True, blank=True)
    valore_obiettivo_totale_in_trattativa = models.FloatField(null=True, blank=True)

    percentuale_di_incremento = models.FloatField(null=True, blank=True)
    ebit_da = models.FloatField(null=True, blank=True)

    any_messi = models.CharField(max_length=500, null=True, blank=True)