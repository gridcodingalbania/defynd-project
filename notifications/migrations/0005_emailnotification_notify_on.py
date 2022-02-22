# Generated by Django 3.1.7 on 2021-05-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20210503_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='notify_on',
            field=models.CharField(choices=[('form_submit', 'Modulo invia'), ('url_click', "Clic sull'URL")], default='form_submit', max_length=21, verbose_name='Notifica sul'),
        ),
    ]
