# Generated by Django 5.0.3 on 2024-03-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_log_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='platform',
            field=models.CharField(default='PC', max_length=20),
        ),
    ]
