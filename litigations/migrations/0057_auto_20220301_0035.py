# Generated by Django 3.1.7 on 2022-02-28 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigations', '0056_auto_20220301_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='upload_pdf',
            field=models.FileField(upload_to='documents/', verbose_name='Upload File'),
        ),
    ]