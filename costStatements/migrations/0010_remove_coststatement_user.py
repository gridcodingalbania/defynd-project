# Generated by Django 3.1.7 on 2021-05-07 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0009_auto_20210506_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coststatement',
            name='user',
        ),
    ]
