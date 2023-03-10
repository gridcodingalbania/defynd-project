# Generated by Django 3.1.7 on 2021-12-02 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costStatements', '0016_coststatement_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coststatement',
            options={'verbose_name': 'cost_statement', 'verbose_name_plural': 'cost_statements'},
        ),
        migrations.AlterModelOptions(
            name='coststatementitem',
            options={'verbose_name': 'cost_statement_item', 'verbose_name_plural': 'cost_statement_items'},
        ),
        migrations.AlterModelOptions(
            name='hypothesis',
            options={'verbose_name': 'hypothesis', 'verbose_name_plural': 'hypothesis_plural'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['priority'], 'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
