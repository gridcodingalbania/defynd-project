# Generated by Django 3.1.7 on 2022-03-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_page', '0014_remove_statistics_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
    ]
