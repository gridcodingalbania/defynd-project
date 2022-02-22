from django.db import models
from django.utils.translation import gettext_lazy as _


class AreaType(models.Model): 
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "area_type"
        verbose_name = _('area-type')
        verbose_name_plural = _('area-types')


class ConstraintType(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "constraint_type"
        verbose_name = _('constraint-type')
        verbose_name_plural = _('constraint-types')


class CultureType(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "culture_type"
        verbose_name = _('culture-type')
        verbose_name_plural = _('culture-types')


class ReclamationInterventionType(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "reclamation_intervention_type"
        verbose_name = _('reclamation-intervention-type')
        verbose_name_plural = _('reclamation-intervention-types')


class UrbanDestination(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "urban_destination"
        verbose_name = _('urban-destination')
        verbose_name_plural = _('urban-destinations')


class DisputeMatter(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "dispute_matter"
        verbose_name = _('dispute-matter')
        verbose_name_plural = _('dispute-matters')


class DisputeObject(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:  
        db_table = "dispute_object"
        verbose_name = _('dispute-object')
        verbose_name_plural = _('dispute-objects')
