# Generated by Django 3.1.7 on 2022-03-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0061_auto_20220303_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]
