# Generated by Django 4.0 on 2022-01-15 14:41

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
            field=models.DateField(default=datetime.date(2022, 1, 15)),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='college',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='college_id',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='pin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregister',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]