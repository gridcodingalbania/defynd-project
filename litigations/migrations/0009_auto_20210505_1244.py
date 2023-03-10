# Generated by Django 3.1.7 on 2021-05-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
        ('litigations', '0008_litigation_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='dispute_matter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.disputematter', verbose_name='Materia Controversia'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='dispute_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.disputeobject', verbose_name='Oggetto Controversia'),
        ),
    ]
