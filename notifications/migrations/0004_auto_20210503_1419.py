# Generated by Django 3.1.7 on 2021-05-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20210503_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='message',
            field=models.TextField(null=True, verbose_name='Messaggio'),
        ),
        migrations.AlterField(
            model_name='emailnotification',
            name='recipients',
            field=models.CharField(blank=True, help_text="separare con; per più di un'e-mail. Se lasciato vuoto,                     verrà utilizzata l'email del modello", max_length=256, null=True, verbose_name='Destinatari'),
        ),
        migrations.AlterField(
            model_name='emailnotification',
            name='subject',
            field=models.CharField(max_length=256, null=True, verbose_name='Soggetto'),
        ),
    ]
