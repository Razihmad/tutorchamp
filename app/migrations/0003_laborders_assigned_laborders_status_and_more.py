# Generated by Django 4.0 on 2022-01-20 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userdetails_profile_alter_orders_submission_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laborders',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laborders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='pending', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laborders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 1, 20)),
        ),
    ]