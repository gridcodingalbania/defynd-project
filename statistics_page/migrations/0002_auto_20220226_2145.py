# Generated by Django 3.1.7 on 2022-02-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='final_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='margine_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='objective_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='revue_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='total_cost_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='total_value',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='initial_value',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Initial Value'),
        ),
    ]