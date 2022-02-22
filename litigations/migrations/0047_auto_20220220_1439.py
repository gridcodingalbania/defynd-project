# Generated by Django 3.1.7 on 2022-02-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0046_auto_20220220_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='litigation',
            name='successful',
        ),
        migrations.AddField(
            model_name='litigation',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Closed'),
        ),
    ]
