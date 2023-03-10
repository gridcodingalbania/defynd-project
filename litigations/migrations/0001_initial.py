# Generated by Django 3.1.7 on 2021-04-28 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import litigations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('configurations', '0001_initial'),
        ('lawyers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Litigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=litigations.models.increment_litigation_number, max_length=20, unique=True, verbose_name='Codice Contenciozo')),
                ('initial_estimation_value', models.FloatField(blank=True, default=0, null=True, verbose_name='Valore Stima Iniziale')),
                ('target_value', models.FloatField(blank=True, default=0, null=True, verbose_name='Valore Obiettivo')),
                ('reference', models.CharField(blank=True, max_length=100, null=True, verbose_name='Riferimento')),
                ('prejudicial_registrations', models.CharField(blank=True, max_length=100, null=True, verbose_name='Iscrizioni Pregiudizievoli')),
                ('registration_type', models.CharField(choices=[(None, ''), ('Esproprio Agricolo', 'Esproprio Agricolo'), ('Esproprio Residenziale Libera', 'Esproprio Residenziale Libera'), ('Esproprio Industriale Libera', 'Esproprio Industriale Libera'), ('Esproprio Fabbricato Residenziale', 'Esproprio Fabbricato Residenziale'), ('Esproprio Fabbricato Industriale', 'Esproprio Fabbricato Industriale')], default=None, max_length=100, null=True, verbose_name='Tipologia Iscrizione')),
                ('enrollment_amount', models.FloatField(blank=True, default=0, null=True, verbose_name='Importo Iscrizione')),
                ('surface_directly_concerned', models.FloatField(blank=True, null=True, verbose_name='Superficie Direttamente Interessata')),
                ('residual_surface', models.FloatField(blank=True, null=True, verbose_name='Superficie Residua')),
                ('technical_reference', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tecnici Riferimento')),
                ('area_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Indirizzo Area')),
                ('reception_act', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Ricezione Atto')),
                ('date_receipt_act', models.DateField(blank=True, null=True, verbose_name='Data Ricezione Atto')),
                ('aboveground_quantification', models.IntegerField(blank=True, help_text='Number of plants', null=True, verbose_name='Quantificazione Soprasuolo')),
                ('fruit_pendants', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Frutti Pendenti')),
                ('cultivator_type', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Tipologia Coltivatore')),
                ('batch_disfiguration', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Sconfigurazione Lotto')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('social_economic_reform', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Tipologia Riforma Economica Sociale (Infrastrutture Strategica)')),
                ('transformation_coefficient', models.IntegerField(blank=True, null=True, verbose_name='Coefficiente di trasformazione (volumi)')),
                ('IMU_final_declaration', models.FloatField(blank=True, null=True, verbose_name='Dichiarazione fini IMU')),
                ('epoch_construction', models.FloatField(blank=True, null=True, verbose_name='Epoca Costruzione (anno)')),
                ('building_titles', models.TextField(blank=True, null=True, verbose_name='Titoli Edilizi')),
                ('contract_date', models.DateField(blank=True, null=True, verbose_name='Data contratto')),
                ('last_notary_fees', models.FloatField(blank=True, null=True, verbose_name='Ultime spese notarili')),
                ('constraints_other_nature', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vincoli altra natura')),
                ('extension_MQ', models.FloatField(blank=True, null=True, verbose_name='Estensione MQ')),
                ('purchase_contract', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name="Contratto d'acquisto")),
                ('residual_airspace', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Cubatura residua')),
                ('MC_residui', models.CharField(blank=True, max_length=100, null=True, verbose_name='MC residui')),
                ('total_demolition', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Demolizione totale')),
                ('partial_demolition', models.CharField(blank=True, max_length=100, null=True, verbose_name='Demolizione parziale')),
                ('storage_state', models.CharField(blank=True, choices=[('great', 'ottimo'), ('good', 'buono'), ('enough', 'sufficiente'), ('to_be_restructured', 'da ristrutturare')], max_length=100, null=True, verbose_name='Stato conservazione')),
                ('productive_activities', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Attivit?? produttive')),
                ('lease_agreement', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Contratto locazione')),
                ('contract_duration', models.FloatField(blank=True, null=True, verbose_name='Durata contratto (mesi)')),
                ('contract_fee', models.FloatField(blank=True, null=True, verbose_name='Canone contratto')),
                ('residual_rent', models.FloatField(blank=True, null=True, verbose_name='Affitto residuo')),
                ('need_transfer_user', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Necessit?? trasferimento utilizzator')),
                ('reclamation_activities', models.CharField(blank=True, choices=[('yes', 'si'), ('no', 'no')], default='no', max_length=100, null=True, verbose_name='Attivit?? di bonifica')),
                ('reclamation_cost', models.FloatField(blank=True, null=True, verbose_name='Costo bonifica')),
                ('area_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.areatype', verbose_name='Tipologia Area')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.customer', verbose_name='Cliente')),
                ('culture_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.culturetype', verbose_name='Tipologia Coltura')),
                ('dispute_matter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.disputematter', verbose_name='Materia Controversia')),
                ('dispute_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.disputeobject', verbose_name='Oggetto Controversia')),
                ('lawyer_reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lawyers.lawyer', verbose_name='Avvocato Riferimento')),
                ('other_constraints_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.constrainttype', verbose_name='Vincoli Altra Natura')),
                ('reclamation_intervention_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.reclamationinterventiontype', verbose_name='Tipologia intervento bonifica')),
                ('urban_destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.urbandestination', verbose_name='Destinazione Urbanistica (come da certificato)')),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utente')),
            ],
            options={
                'db_table': 'litigation',
                'ordering': ['name'],
            },
        ),
    ]
