# Generated by Django 3.1.7 on 2022-03-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_page', '0022_statistics_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='title',
            field=models.IntegerField(default=1, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
