# Generated by Django 3.1.7 on 2022-02-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0034_auto_20220209_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigation',
            name='contract',
            field=models.BooleanField(default=True),
        ),
    ]
