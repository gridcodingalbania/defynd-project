# Generated by Django 3.1.7 on 2021-04-30 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20210430_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
