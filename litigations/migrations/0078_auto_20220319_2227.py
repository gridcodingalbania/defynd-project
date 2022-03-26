# Generated by Django 3.1.7 on 2022-03-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0077_auto_20220319_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='litigation',
            name='turnover_margin',
        ),
        migrations.AddField(
            model_name='litigation',
            name='EBIT',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='EBIT'),
        ),
    ]