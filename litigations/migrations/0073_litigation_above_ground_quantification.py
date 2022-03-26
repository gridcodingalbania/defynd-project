# Generated by Django 3.1.7 on 2022-03-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0072_remove_litigation_above_ground_quantification'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigation',
            name='above_ground_quantification',
            field=models.IntegerField(blank=True, default=0, help_text='Plant Name', null=True, verbose_name='Above Ground Quantification'),
        ),
    ]