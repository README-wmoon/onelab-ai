# Generated by Django 5.0.2 on 2024-05-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_title',
            field=models.TextField(),
        ),
    ]
