# Generated by Django 3.2.5 on 2021-12-18 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2021, 12, 19)),
        ),
    ]
