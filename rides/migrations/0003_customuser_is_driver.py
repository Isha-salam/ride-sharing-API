# Generated by Django 5.1.7 on 2025-03-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]
