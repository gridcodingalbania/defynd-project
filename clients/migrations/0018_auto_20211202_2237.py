# Generated by Django 3.1.7 on 2021-12-02 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_remove_customer_fiscal_code_individual'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
    ]
