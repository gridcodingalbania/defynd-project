# Generated by Django 3.1.7 on 2022-02-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0050_auto_20220226_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigation',
            name='revenue',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Revenue'),
        ),
        migrations.AddField(
            model_name='litigation',
            name='total_cost',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Cost'),
        ),
        migrations.AddField(
            model_name='litigation',
            name='turnover_margin',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Turnover Margin'),
        ),
    ]
