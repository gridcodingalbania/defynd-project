# Generated by Django 3.1.7 on 2021-12-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0017_auto_20211202_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coststatement',
            name='expected_dealing_term',
            field=models.IntegerField(null=True, verbose_name='Termine previsto negoziazione'),
        ),
    ]
