# Generated by Django 4.0 on 2022-03-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatter', '0004_auto_20220307_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
