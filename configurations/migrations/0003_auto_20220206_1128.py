# Generated by Django 3.1.7 on 2022-02-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_auto_20211202_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areatype',
            options={'verbose_name': 'area-type', 'verbose_name_plural': 'area-types'},
        ),
        migrations.AlterModelOptions(
            name='constrainttype',
            options={'verbose_name': 'constraint-type', 'verbose_name_plural': 'constraint-types'},
        ),
        migrations.AlterModelOptions(
            name='culturetype',
            options={'verbose_name': 'culture-type', 'verbose_name_plural': 'culture-types'},
        ),
        migrations.AlterModelOptions(
            name='disputematter',
            options={'verbose_name': 'dispute-matter', 'verbose_name_plural': 'dispute-matters'},
        ),
        migrations.AlterModelOptions(
            name='disputeobject',
            options={'verbose_name': 'dispute-object', 'verbose_name_plural': 'dispute-objects'},
        ),
        migrations.AlterModelOptions(
            name='reclamationinterventiontype',
            options={'verbose_name': 'reclamation-intervention-type', 'verbose_name_plural': 'reclamation-intervention-types'},
        ),
        migrations.AlterModelOptions(
            name='urbandestination',
            options={'verbose_name': 'urban-destination', 'verbose_name_plural': 'urban-destinations'},
        ),
        migrations.AlterField(
            model_name='areatype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='constrainttype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='culturetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='disputematter',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='disputeobject',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='reclamationinterventiontype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='urbandestination',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
