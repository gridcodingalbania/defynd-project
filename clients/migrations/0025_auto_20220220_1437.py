# Generated by Django 3.1.7 on 2022-02-20 13:37

import clients.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0024_auto_20220209_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birthplace',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Birth-place'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=256, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(default=clients.models.increment_customer_number, max_length=20, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(choices=[('individual', 'Individuo'), ('company', 'Azienda')], default='individual', max_length=16, null=True, verbose_name='Customer Type'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fiscal_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Fiscal Code'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, ''), ('F', 'Femmina'), ('M', 'Maschio')], default=None, max_length=10, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_customer',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Is Customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='post_number',
            field=models.CharField(max_length=100, null=True, verbose_name='Post Number'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(max_length=256, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vat_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Vat Number'),
        ),
    ]
