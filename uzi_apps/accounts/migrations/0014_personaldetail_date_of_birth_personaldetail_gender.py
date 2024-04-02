# Generated by Django 5.0.3 on 2024-04-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_personaldetail_marital_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FAMALE', 'FAMALE')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]