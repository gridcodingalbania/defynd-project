# Generated by Django 3.1.7 on 2022-03-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0069_auto_20220307_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='upload_pdf',
            field=models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Upload Contract'),
        ),
    ]
