# Generated by Django 4.0 on 2022-01-20 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_orders_submission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 1, 20)),
        ),
    ]
