# Generated by Django 3.1.7 on 2022-02-04 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_auto_20220204_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contact_phone',
            new_name='phone',
        ),
    ]
