# Generated by Django 4.0 on 2022-02-22 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_questions_laborders_order_id_orders_order_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'managed': True, 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelTable(
            name='questions',
            table='',
        ),
    ]
