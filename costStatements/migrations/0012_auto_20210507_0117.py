# Generated by Django 3.1.7 on 2021-05-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0011_auto_20210507_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='coststatement',
            name='expected_dealing_term',
            field=models.IntegerField(null=True, verbose_name='Termine previsto negoziazione '),
        ),
        migrations.AddField(
            model_name='coststatement',
            name='init_negotiation',
            field=models.IntegerField(null=True, verbose_name='Inizio negoziazione'),
        ),
    ]
