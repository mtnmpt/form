# Generated by Django 5.1.6 on 2025-02-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
