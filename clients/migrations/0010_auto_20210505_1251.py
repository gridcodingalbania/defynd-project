# Generated by Django 3.1.7 on 2021-05-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20210505_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Indirizzo e-mail'),
        ),
    ]
