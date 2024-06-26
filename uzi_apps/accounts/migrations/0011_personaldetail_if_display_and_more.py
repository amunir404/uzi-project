# Generated by Django 5.0.3 on 2024-04-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_personaldetail_profile_alter_personaldetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='if_display',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
