# Generated by Django 3.1.7 on 2022-02-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0051_auto_20220226_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='revenue',
            field=models.IntegerField(blank=True, null=True, verbose_name='Revenue'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='total_cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Cost'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='turnover_margin',
            field=models.IntegerField(blank=True, null=True, verbose_name='Turnover Margin'),
        ),
    ]
