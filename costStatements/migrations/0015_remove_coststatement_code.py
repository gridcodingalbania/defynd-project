# Generated by Django 3.1.7 on 2021-05-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0014_auto_20210507_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coststatement',
            name='code',
        ),
    ]
