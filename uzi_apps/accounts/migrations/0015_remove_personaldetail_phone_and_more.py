# Generated by Django 5.0.3 on 2024-04-02 07:57

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_personaldetail_date_of_birth_personaldetail_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='phone',
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
