# Generated by Django 5.0.3 on 2024-04-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_partner_partner_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_code',
            field=models.CharField(blank=True, default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
