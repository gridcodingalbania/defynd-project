# Generated by Django 3.1.7 on 2021-05-07 12:54

import costStatements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0013_auto_20210507_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coststatement',
            name='code',
            field=models.CharField(max_length=100, null=True, verbose_name='Codice'),
        ),
        migrations.AlterField(
            model_name='coststatement',
            name='name',
            field=models.CharField(default=costStatements.models.increment_costStatement_number, max_length=100, null=True, verbose_name='Nome'),
        ),
    ]
