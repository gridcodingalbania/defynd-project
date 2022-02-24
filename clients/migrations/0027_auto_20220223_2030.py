# Generated by Django 3.1.7 on 2022-02-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0026_customer_phone_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='Phone'),
        ),
    ]
