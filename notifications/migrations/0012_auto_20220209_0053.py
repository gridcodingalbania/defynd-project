# Generated by Django 3.1.7 on 2022-02-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0011_auto_20220206_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoingmailserver',
            name='port',
            field=models.CharField(max_length=8, verbose_name='port'),
        ),
        migrations.AlterField(
            model_name='outgoingmailserver',
            name='security_type',
            field=models.CharField(blank=True, choices=[(None, ''), ('TLS', 'TLS'), ('SSL', 'SSL')], default=None, max_length=10, null=True, verbose_name='security-type'),
        ),
        migrations.AlterField(
            model_name='outgoingmailserver',
            name='server',
            field=models.CharField(max_length=64, verbose_name='server-host'),
        ),
    ]
