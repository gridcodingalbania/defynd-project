# Generated by Django 3.1.7 on 2021-10-31 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_auto_20211031_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fisc_code',
            new_name='fiscal_code',
        ),
    ]
