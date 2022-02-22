# Generated by Django 3.1.7 on 2021-11-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0012_auto_20211101_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='initial_estimation_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, null=True, verbose_name='Valore Stima Iniziale'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='target_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, null=True, verbose_name='Valore Obiettivo'),
        ),
    ]
