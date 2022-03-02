# Generated by Django 4.0 on 2022-03-02 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laborders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='laborders',
            name='status',
            field=models.CharField(choices=[('Awaiting Confirmation', 'Awaiting Confirmation'), ('Order Confirmed', 'Order Confirmed'), ('Order Rejected', 'Order Rejected'), ('Assignment In Progress', 'Assignment In Progress'), ('Review Your Assignment', 'Review Your Assignment'), ('Assignment Under Revision', 'Assignment Under Revision'), ('Assignment Completed', 'Assignment Completed')], max_length=100),
        ),
        migrations.AlterField(
            model_name='laborders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 3, 2)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Awaiting Confirmation', 'Awaiting Confirmation'), ('Order Confirmed', 'Order Confirmed'), ('Order Rejected', 'Order Rejected'), ('Assignment In Progress', 'Assignment In Progress'), ('Review Your Assignment', 'Review Your Assignment'), ('Assignment Under Revision', 'Assignment Under Revision'), ('Assignment Completed', 'Assignment Completed')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='submission_date',
            field=models.DateField(default=datetime.date(2022, 3, 2)),
        ),
    ]