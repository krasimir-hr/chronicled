# Generated by Django 5.0.3 on 2024-03-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_log_completed_alter_log_first_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
