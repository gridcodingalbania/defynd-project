# Generated by Django 3.1.7 on 2021-05-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0007_itemcategory_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='include_in_cost',
        ),
    ]
