# Generated by Django 3.1.7 on 2021-05-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20210503_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoingmailserver',
            name='security_type',
            field=models.CharField(blank=True, choices=[(None, ''), ('TLS', 'TLS'), ('SSL', 'SSL')], default=None, max_length=10, null=True, verbose_name='Security Type'),
        ),
    ]
