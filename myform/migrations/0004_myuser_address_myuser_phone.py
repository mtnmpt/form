# Generated by Django 5.1.6 on 2025-02-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0003_remove_myuser_address_remove_myuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
