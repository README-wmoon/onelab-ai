# Generated by Django 5.0.2 on 2024-03-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_alter_alarm_alarm_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]