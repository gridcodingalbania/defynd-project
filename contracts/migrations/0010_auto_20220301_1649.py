# Generated by Django 3.1.7 on 2022-03-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_auto_20220301_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='url',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Url'),
        ),
    ]