# Generated by Django 5.0.3 on 2024-04-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_rename_partner_referral_partner_partner_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_code',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
