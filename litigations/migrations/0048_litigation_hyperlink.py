# Generated by Django 3.1.7 on 2022-02-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0047_auto_20220220_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigation',
            name='hyperlink',
            field=models.URLField(blank=True, max_length=7000, null=True, verbose_name='HyperLink to Economics Sheet'),
        ),
    ]
