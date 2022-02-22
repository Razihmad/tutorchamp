# Generated by Django 4.0 on 2022-02-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_questions_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='subject',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Maths', 'Maths'), ('Essay Writing', 'Essay Writing'), ('Chemistry', 'Chemistry'), ('Accounting', 'Accounting'), ('Economics', 'Economics'), ('Management', 'Management'), ('Biology', 'Biology'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science', 'Computer Science'), ('Nursing', 'Nursing'), ('Electrical', 'Electrical'), ('Mechanical', 'Mechanical'), ('Finance', 'Finance'), ('Civil Engineering', 'Civil Engineering')], max_length=100),
        ),
    ]