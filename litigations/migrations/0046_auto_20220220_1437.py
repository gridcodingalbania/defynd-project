# Generated by Django 3.1.7 on 2022-02-20 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0007_auto_20220212_2051'),
        ('litigations', '0045_auto_20220220_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='IMU_final_declaration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Fianl Declaration IMU'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='MC_residui',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='MC Residui'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='building_titles',
            field=models.TextField(blank=True, null=True, verbose_name='Building Titles'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='constraints_other_nature',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Constraints Other Nture'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='contract_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Date'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='contract_duration',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Contract Duration'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='contract_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, null=True, verbose_name='Contract fee'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='epoch_construction',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Epoch Constrution'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='extension_MQ',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='Eextension MQ'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='last_notary_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Last Notary Fees'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='lease_agreement',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Lease Agreement'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='need_transfer_user',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Nees Transfer User'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='partial_demolition',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Partial Demolition'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='productive_activities',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Productive Activities'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='purchase_contract',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Purchase Constract'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='reclamation_activities',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Reclamation Activities'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='reclamation_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=32, null=True, verbose_name='Reclamation Cost'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='reclamation_intervention_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.reclamationinterventiontype', verbose_name='Reclamation Intervention Type'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='residual_airspace',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Residual Airspace'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='residual_rent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, null=True, verbose_name='Residual Rent'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='social_economic_reform',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Social Economic Reform'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='storage_state',
            field=models.CharField(blank=True, choices=[('great', 'ottimo'), ('good', 'buono'), ('enough', 'sufficiente'), ('to_be_restructured', 'da ristrutturare')], max_length=100, null=True, verbose_name='Storage State'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='target_date',
            field=models.DateField(max_length=100, null=True, verbose_name='Target Data'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='total_demolition',
            field=models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Total Demolition'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='transformation_coefficient',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Transformation Coefficient'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='urban_destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.urbandestination', verbose_name='Urban Destination'),
        ),
    ]
