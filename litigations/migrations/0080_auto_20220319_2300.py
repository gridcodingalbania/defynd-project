# Generated by Django 3.1.7 on 2022-03-19 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0079_auto_20220319_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='litigation',
            old_name='EBIT',
            new_name='turnover_margin',
        ),
    ]