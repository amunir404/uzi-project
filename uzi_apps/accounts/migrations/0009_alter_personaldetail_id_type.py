# Generated by Django 5.0.3 on 2024-04-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_personaldetail_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='id_type',
            field=models.CharField(choices=[('IDCARD', 'KTP'), ('PASSPORT', 'PASSPORT'), ('DRIVING_LICENSE', 'DRIVING LICENSE')], default='IDCARD', max_length=20),
        ),
    ]