# Generated by Django 3.1.7 on 2022-03-06 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_page', '0018_auto_20220306_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='title',
        ),
    ]