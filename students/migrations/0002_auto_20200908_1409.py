# Generated by Django 3.1 on 2020-09-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
