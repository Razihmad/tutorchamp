# Generated by Django 2.2.27 on 2022-03-08 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laborders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 3, 8)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 3, 8)),
        ),
    ]