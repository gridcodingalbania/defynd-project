# Generated by Django 3.1.7 on 2022-02-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0038_auto_20220212_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='litigation',
            name='reopen',
        ),
        migrations.AddField(
            model_name='litigation',
            name='clossed',
            field=models.BooleanField(default=True, verbose_name='clossed'),
        ),
    ]
