# Generated by Django 3.1.7 on 2022-02-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_auto_20211202_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='contact_phone',
        ),
    ]
