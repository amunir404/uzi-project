# Generated by Django 5.0.3 on 2024-03-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('INVESTOR', 'INVESTOR'), ('PARTNER', 'PARTNER')], default='INVESTOR', max_length=20),
        ),
    ]