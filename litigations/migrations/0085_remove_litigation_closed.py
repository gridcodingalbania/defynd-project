# Generated by Django 3.1.7 on 2022-03-20 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0084_auto_20220320_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='litigation',
            name='closed',
        ),
    ]