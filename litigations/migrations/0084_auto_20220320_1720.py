# Generated by Django 3.1.7 on 2022-03-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0083_auto_20220320_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='value_list',
            field=models.CharField(blank=True, choices=[('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('90%', '90%'), ('100%', '100%')], default='no', max_length=100, null=True, verbose_name='Value List'),
        ),
    ]
