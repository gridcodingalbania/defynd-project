# Generated by Django 3.1.7 on 2021-05-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0007_auto_20210505_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigation',
            name='origin',
            field=models.CharField(blank=True, choices=[('internal', 'interno'), ('web', 'web')], default='internal', max_length=8, null=True, verbose_name='Origine'),
        ),
    ]
