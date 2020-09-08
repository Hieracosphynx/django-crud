# Generated by Django 3.1 on 2020-09-04 04:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200903_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number', regex='^\\+\\d{9,15}$')]),
        ),
    ]