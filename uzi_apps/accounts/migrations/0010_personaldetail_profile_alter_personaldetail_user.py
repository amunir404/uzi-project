# Generated by Django 5.0.3 on 2024-04-02 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_personaldetail_id_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='personaldetail', to='accounts.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personaldetail', to=settings.AUTH_USER_MODEL),
        ),
    ]
